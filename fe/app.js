// API Configuration
const API_BASE_URL = 'http://localhost:8000/api';

// Global variables
let map;
let markers = [];
let allSinkholes = [];

// Risk level colors
const RISK_COLORS = {
    'low': '#4caf50',
    'LOW': '#4caf50',
    'medium': '#ff9800',
    'MEDIUM': '#ff9800',
    'high': '#ff5722',
    'HIGH': '#ff5722',
    'critical': '#f44336',
    'CRITICAL': '#f44336'
};

// Initialize the map
function initMap() {
    // Center on Rome, Italy where the detected sinkholes are located
    map = L.map('map').setView([41.90, 12.50], 12);
    // map = L.map('map').setView([20, 0], 2); //center = world view
    
    // Add dark theme tile layer
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        maxZoom: 19
    }).addTo(map);
}

// Create custom marker
function createMarker(sinkhole) {
    const color = RISK_COLORS[sinkhole.risk_level];
    
    const marker = L.circleMarker([sinkhole.latitude, sinkhole.longitude], {
        radius: Math.min(10, Math.max(4, Math.log(sinkhole.diameter) * 2)),
        fillColor: color,
        color: '#fff',
        weight: 2,
        opacity: 0.8,
        fillOpacity: 0.6
    });
    
    // Create popup content
    const popupContent = `
        <div class="sinkhole-popup">
            <h3>${sinkhole.name}</h3>
            <p><strong>Risk Level:</strong> <span style="color: ${color}">${sinkhole.risk_level}</span></p>
            <p><strong>Type:</strong> ${sinkhole.geological_type}</p>
            <p><strong>Diameter:</strong> ${sinkhole.diameter.toFixed(1)}m</p>
            <p><strong>Depth:</strong> ${sinkhole.depth.toFixed(1)}m</p>
            ${sinkhole.soil_type ? `<p><strong>Soil Type:</strong> ${sinkhole.soil_type}</p>` : ''}
            ${sinkhole.bedrock_type ? `<p><strong>Bedrock:</strong> ${sinkhole.bedrock_type}</p>` : ''}
            ${sinkhole.water_table_depth ? `<p><strong>Water Table Depth:</strong> ${sinkhole.water_table_depth.toFixed(1)}m</p>` : ''}
            <p><strong>Status:</strong> ${sinkhole.is_active ? '🔴 Active' : '⚫ Inactive'}</p>
            ${sinkhole.discovery_date ? `<p><strong>Discovered:</strong> ${new Date(sinkhole.discovery_date).toLocaleDateString()}</p>` : ''}
            ${sinkhole.description ? `<p style="margin-top: 10px; font-style: italic;">${sinkhole.description}</p>` : ''}
        </div>
    `;
    
    marker.bindPopup(popupContent);
    marker.sinkhole = sinkhole; // Store reference
    
    return marker;
}

// Fetch sinkholes from API
async function fetchSinkholes() {
    try {
        // Try to fetch from API first
        console.log('Attempting to fetch from API:', `${API_BASE_URL}/sinkholes/`);
        const response = await fetch(`${API_BASE_URL}/sinkholes/`);
        if (!response.ok) throw new Error('Failed to fetch sinkholes');
        const data = await response.json();
        console.log('Successfully loaded data from API:', data.length, 'sinkholes');
        allSinkholes = data;
        displayMarkers();
    } catch (error) {
        console.log('API not available, trying static data...', error.message);
        // Fallback to static JSON file for GitHub Pages deployment
        try {
            console.log('Fetching static data from: sinkholes-data.json');
            const response = await fetch('sinkholes-data.json');
            console.log('Static data response status:', response.status, response.ok);
            if (!response.ok) throw new Error('Failed to fetch static data');
            const data = await response.json();
            console.log('Successfully loaded static data:', data.length, 'sinkholes');
            allSinkholes = data;
            displayMarkers();
        } catch (staticError) {
            console.error('Error fetching static data:', staticError);
            console.error('Original API error:', error);
            alert('Failed to load sinkhole data. Make sure the backend server is running or static data is available.');
        }
    }
}

// Fetch statistics from API
async function fetchStatistics() {
    try {
        const response = await fetch(`${API_BASE_URL}/sinkholes/statistics/`);
        if (!response.ok) throw new Error('Failed to fetch statistics');
        const data = await response.json();
        displayStatistics(data);
    } catch (error) {
        console.log('API statistics not available, calculating from loaded data...');
        // Calculate statistics from loaded sinkholes
        if (allSinkholes && allSinkholes.length > 0) {
            calculateStatistics();
        }
    }
}

// Calculate statistics from loaded sinkhole data
function calculateStatistics() {
    const stats = {
        total_count: allSinkholes.length,
        active_count: allSinkholes.filter(s => s.is_active).length,
        average_diameter: (allSinkholes.reduce((sum, s) => sum + (s.diameter || 0), 0) / allSinkholes.length).toFixed(1),
        average_depth: (allSinkholes.reduce((sum, s) => sum + (s.depth || 0), 0) / allSinkholes.length).toFixed(1),
        risk_distribution: [],
        geological_distribution: []
    };
    
    // Calculate risk distribution
    const riskCounts = {};
    const geoCounts = {};
    
    allSinkholes.forEach(s => {
        const risk = (s.risk_level || 'unknown').toUpperCase();
        const geo = s.geological_type || 'unknown';
        riskCounts[risk] = (riskCounts[risk] || 0) + 1;
        geoCounts[geo] = (geoCounts[geo] || 0) + 1;
    });
    
    stats.risk_distribution = Object.entries(riskCounts).map(([risk_level, count]) => ({ risk_level, count }));
    stats.geological_distribution = Object.entries(geoCounts).map(([geological_type, count]) => ({ geological_type, count }));
    
    displayStatistics(stats);
}

// Display statistics
function displayStatistics(stats) {
    document.getElementById('total-count').textContent = stats.total_count;
    document.getElementById('active-count').textContent = stats.active_count;
    document.getElementById('avg-diameter').textContent = `${stats.average_diameter}m`;
    document.getElementById('avg-depth').textContent = `${stats.average_depth}m`;
    
    // Display risk chart
    const riskChart = document.getElementById('risk-chart');
    riskChart.innerHTML = '';
    const maxRiskCount = Math.max(...stats.risk_distribution.map(r => r.count));
    
    stats.risk_distribution.forEach(item => {
        const width = (item.count / maxRiskCount) * 100;
        const bar = document.createElement('div');
        bar.className = 'chart-bar';
        bar.innerHTML = `
            <span class="chart-label">${item.risk_level}</span>
            <div class="chart-bar-fill" style="width: ${width}%; background: ${RISK_COLORS[item.risk_level]};">
                ${item.count}
            </div>
        `;
        riskChart.appendChild(bar);
    });
    
    // Display geological chart
    const geoChart = document.getElementById('geological-chart');
    geoChart.innerHTML = '';
    const maxGeoCount = Math.max(...stats.geological_distribution.map(g => g.count));
    
    const geoColors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6'];
    
    stats.geological_distribution.forEach((item, index) => {
        const width = (item.count / maxGeoCount) * 100;
        const bar = document.createElement('div');
        bar.className = 'chart-bar';
        bar.innerHTML = `
            <span class="chart-label">${item.geological_type}</span>
            <div class="chart-bar-fill" style="width: ${width}%; background: ${geoColors[index % geoColors.length]};">
                ${item.count}
            </div>
        `;
        geoChart.appendChild(bar);
    });
}

// Display markers on map
function displayMarkers() {
    // Clear existing markers
    markers.forEach(marker => map.removeLayer(marker));
    markers = [];
    
    console.log('Total sinkholes loaded:', allSinkholes.length);
    
    // Get filter settings
    const showAll = document.getElementById('layer-all').checked;
    const activeOnly = document.getElementById('filter-active').checked;
    
    const riskFilters = Array.from(document.querySelectorAll('.risk-filter:checked'))
        .map(cb => cb.value.toLowerCase());
    const typeFilters = Array.from(document.querySelectorAll('.type-filter:checked'))
        .map(cb => cb.value);
    
    console.log('Show all:', showAll, 'Active only:', activeOnly);
    console.log('Risk filters:', riskFilters);
    console.log('Type filters:', typeFilters);
    
    // Filter and display sinkholes
    const filteredSinkholes = allSinkholes.filter(sinkhole => {
        if (!showAll) return false;
        if (activeOnly && !sinkhole.is_active) return false;
        if (sinkhole.risk_level && !riskFilters.includes(sinkhole.risk_level.toLowerCase())) return false;
        if (sinkhole.geological_type && !typeFilters.includes(sinkhole.geological_type)) return false;
        return true;
    });
    
    console.log('Filtered sinkholes:', filteredSinkholes.length);
    
    filteredSinkholes.forEach(sinkhole => {
        const marker = createMarker(sinkhole);
        marker.addTo(map);
        markers.push(marker);
    });
    
    // Update statistics based on filtered sinkholes
    updateStatisticsForFiltered(filteredSinkholes);
    
    // Auto-zoom to fit all markers
    if (markers.length > 0) {
        const group = new L.featureGroup(markers);
        map.fitBounds(group.getBounds().pad(0.1));
    }
}

// Update statistics based on currently filtered sinkholes
function updateStatisticsForFiltered(sinkholes) {
    if (!sinkholes || sinkholes.length === 0) {
        // Show zeros if no sinkholes are visible
        document.getElementById('total-count').textContent = '0';
        document.getElementById('active-count').textContent = '0';
        document.getElementById('avg-diameter').textContent = '0m';
        document.getElementById('avg-depth').textContent = '0m';
        document.getElementById('risk-chart').innerHTML = '<p style="color: #999;">No data</p>';
        document.getElementById('geological-chart').innerHTML = '<p style="color: #999;">No data</p>';
        return;
    }
    
    const stats = {
        total_count: sinkholes.length,
        active_count: sinkholes.filter(s => s.is_active).length,
        average_diameter: (sinkholes.reduce((sum, s) => sum + (s.diameter || 0), 0) / sinkholes.length).toFixed(1),
        average_depth: (sinkholes.reduce((sum, s) => sum + (s.depth || 0), 0) / sinkholes.length).toFixed(1),
        risk_distribution: [],
        geological_distribution: []
    };
    
    // Calculate risk distribution
    const riskCounts = {};
    const geoCounts = {};
    
    sinkholes.forEach(s => {
        const risk = (s.risk_level || 'unknown').toUpperCase();
        const geo = s.geological_type || 'unknown';
        riskCounts[risk] = (riskCounts[risk] || 0) + 1;
        geoCounts[geo] = (geoCounts[geo] || 0) + 1;
    });
    
    stats.risk_distribution = Object.entries(riskCounts).map(([risk_level, count]) => ({ risk_level, count }));
    stats.geological_distribution = Object.entries(geoCounts).map(([geological_type, count]) => ({ geological_type, count }));
    
    displayStatistics(stats);
}

// Set up event listeners
function setupEventListeners() {
    // Layer controls
    document.getElementById('layer-all').addEventListener('change', displayMarkers);
    document.getElementById('filter-active').addEventListener('change', displayMarkers);
    
    document.querySelectorAll('.risk-filter').forEach(cb => {
        cb.addEventListener('change', displayMarkers);
    });
    
    document.querySelectorAll('.type-filter').forEach(cb => {
        cb.addEventListener('change', displayMarkers);
    });
}

// Initialize dashboard
async function init() {
    initMap();
    setupEventListeners();
    await fetchSinkholes();
    await fetchStatistics();
}

// Start the application when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}
