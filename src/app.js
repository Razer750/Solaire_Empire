// Chargement et affichage dynamique des données

// Configuration
const DATA_SOURCES = {
    catalogue: '../data/catalogue.json',
    videos: '../agents/results_gemini_web.json'
};

// Initialisation au chargement de la page
document.addEventListener('DOMContentLoaded', () => {
    loadCatalogue();
    loadProjets();
    loadVideos();
    setupContactForm();
    setupScrollAnimations();
});

// === CATALOGUE PRODUITS ===
async function loadCatalogue() {
    try {
        const response = await fetch(DATA_SOURCES.catalogue);
        const data = await response.json();

        const productsGrid = document.getElementById('products-grid');
        productsGrid.innerHTML = '';

        data.produits.forEach(product => {
            const card = createProductCard(product);
            productsGrid.appendChild(card);
        });

        console.log(`✓ ${data.produits.length} produits chargés`);
    } catch (error) {
        console.error('Erreur chargement catalogue:', error);
        showFallbackProducts();
    }
}

function createProductCard(product) {
    const card = document.createElement('div');
    card.className = 'product-card';

    const stockBadge = product.stock_france
        ? '<span class="product-stock">✓ Stock France 🇫🇷</span>'
        : '<span class="product-stock unavailable">Sur commande</span>';

    // Badge Classe A pour Honstar
    const classeABadge = product.marque === 'Honstar'
        ? '<span class="classe-a-badge">🛡️ CLASSE A</span>'
        : '';

    // Badge 300 couleurs
    const couleursBadge = '<span class="couleurs-badge">🎨 300 Couleurs</span>';

    card.innerHTML = `
        <div class="product-header">
            <span class="product-ref">${product.ref}</span>
            ${stockBadge}
        </div>

        ${classeABadge}
        ${couleursBadge}

        <h3 class="product-title">${product.marque}</h3>
        <p class="product-tech">Technologie ${product.technologie}</p>

        <div class="product-specs">
            ⚡ Puissance: <strong>${product.puissance_w}W</strong><br>
            📊 Rendement: <strong>${product.specs.rendement}</strong><br>
            📐 Dimensions: <strong>${product.specs.dimensions}</strong><br>
            🛡️ Garantie: <strong>${product.specs.garanties}</strong><br>
            🎨 Options: <strong>300 couleurs disponibles</strong>
        </div>

        <div class="product-price">
            ${product.prix_ht}€ <span>HT / panneau</span>
        </div>

        <div class="product-arguments">
            ${product.arguments.map(arg => `<span class="argument-badge">${arg}</span>`).join('')}
        </div>

        <button class="cta-button primary" style="width: 100%; margin-top: 1rem; padding: 1rem;" onclick="demanderDevis('${product.ref}')">
            📞 Demander un devis
        </button>
    `;

    return card;
}

function showFallbackProducts() {
    const productsGrid = document.getElementById('products-grid');
    productsGrid.innerHTML = `
        <div class="product-card">
            <p style="text-align: center; padding: 2rem;">
                Chargement du catalogue...<br>
                <small>Vérifiez que data/catalogue.json est accessible</small>
            </p>
        </div>
    `;
}

// === PROJETS RÉFÉRENCES ===
async function loadProjets() {
    try {
        const response = await fetch('../agents/results_gemini_web.json');
        const data = await response.json();

        const projetsGrid = document.getElementById('projets-grid');
        if (!projetsGrid) return;

        projetsGrid.innerHTML = '';

        // Récupère les projets références
        const projets = data.results[0]?.projets_references || [];

        projets.forEach(projet => {
            const card = createProjetCard(projet);
            projetsGrid.appendChild(card);
        });

        console.log(`✓ ${projets.length} projets références chargés`);
    } catch (error) {
        console.error('Erreur chargement projets:', error);
    }
}

function createProjetCard(projet) {
    const card = document.createElement('div');
    card.className = 'projet-card';

    card.innerHTML = `
        <div class="projet-header">
            <h3 class="projet-nom">${projet.nom}</h3>
            <span class="projet-puissance">${projet.puissance_mwc} MWc</span>
        </div>

        <p class="projet-localisation">${projet.localisation}</p>

        <div class="projet-tech">
            ${projet.technologie}
        </div>

        <ul class="projet-highlights">
            ${projet.highlights.map(highlight => `<li>${highlight}</li>`).join('')}
        </ul>

        <span class="projet-annee">${projet.annee}</span>
    `;

    return card;
}

// === VIDÉOS ===
async function loadVideos() {
    try {
        const response = await fetch(DATA_SOURCES.videos);
        const data = await response.json();

        const videosGrid = document.getElementById('videos-grid');
        videosGrid.innerHTML = '';

        // Récupère les vidéos depuis les résultats de Gemini
        const videos = data.results[0].videos || data.results.videos || [];

        videos.forEach(video => {
            const card = createVideoCard(video, data.results[0].scripts);
            videosGrid.appendChild(card);
        });

        console.log(`✓ ${videos.length} vidéos chargées`);
    } catch (error) {
        console.error('Erreur chargement vidéos:', error);
        showFallbackVideos();
    }
}

function createVideoCard(video, scripts) {
    const card = document.createElement('div');
    card.className = 'video-card';

    // Trouve le script correspondant
    const script = scripts?.find(s => s.video_id === video.url.split('v=')[1]) || {};

    // Icône selon le type
    const typeIcons = {
        'reel': '🎬',
        'demo': '🔧',
        'tutoriel': '📚'
    };

    card.innerHTML = `
        <div class="video-thumbnail">
            ${typeIcons[video.type] || '▶️'}
        </div>

        <div class="video-info">
            <span class="video-type">${video.type}</span>
            <h3 class="video-title">${video.titre}</h3>
            <p class="video-script">
                ${script.texte || 'Découvrez nos panneaux solaires CdTe en action.'}
            </p>
            ${script.message_cle ? `<p style="color: var(--accent); margin-top: 1rem; font-weight: bold;">💡 ${script.message_cle}</p>` : ''}

            <a href="${video.url}" target="_blank" class="cta-button" style="display: inline-block; margin-top: 1rem; padding: 0.5rem 1.5rem; font-size: 0.9rem;">
                Voir la vidéo
            </a>
        </div>
    `;

    return card;
}

function showFallbackVideos() {
    const videosGrid = document.getElementById('videos-grid');
    videosGrid.innerHTML = `
        <div class="video-card">
            <div class="video-thumbnail">🎬</div>
            <div class="video-info">
                <span class="video-type">reel</span>
                <h3 class="video-title">Révolution CdTe</h3>
                <p class="video-script">Découvrez pourquoi le CdTe change tout.</p>
            </div>
        </div>
    `;
}

// === FORMULAIRE CONTACT ===
function setupContactForm() {
    const form = document.querySelector('.contact-form');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const data = Object.fromEntries(formData);

        console.log('Demande de devis:', data);

        // Simulation envoi (à remplacer par vraie API)
        const button = form.querySelector('button');
        const originalText = button.textContent;

        button.textContent = '⏳ Envoi en cours...';
        button.disabled = true;

        setTimeout(() => {
            button.textContent = '✓ Demande envoyée !';
            button.style.background = '#00ff00';

            setTimeout(() => {
                button.textContent = originalText;
                button.disabled = false;
                button.style.background = '';
                form.reset();
            }, 2000);
        }, 1500);
    });
}

function demanderDevis(ref) {
    // Scroll vers le formulaire et pré-remplit la référence
    document.getElementById('contact').scrollIntoView({ behavior: 'smooth' });

    setTimeout(() => {
        const form = document.querySelector('.contact-form');
        const textarea = form.querySelector('textarea');
        textarea.value = `Je souhaite un devis pour le panneau ${ref}.`;
        textarea.focus();
    }, 500);
}

// === ANIMATIONS SCROLL ===
function setupScrollAnimations() {
    // Parallax hero
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const heroContent = document.querySelector('.hero-content');

        if (heroContent) {
            heroContent.style.transform = `translateY(${scrolled * 0.3}px)`;
            heroContent.style.opacity = 1 - scrolled / 600;
        }
    });

    // Fade in au scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    // Observer les cartes
    document.querySelectorAll('.product-card, .projet-card, .video-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s, transform 0.6s';
        observer.observe(el);
    });
}

// === EASTER EGG: Console Message ===
console.log('%c⚡ SOLAIRE EMPIRE', 'font-size: 30px; font-weight: bold; color: #FFD700;');
console.log('%cRévolution CdTe activée ✓', 'font-size: 14px; color: #00D4FF;');
console.log('%cLess cher • Plus beau • Stock France', 'font-size: 12px; color: #fff;');
console.log('\n📊 Architecture Multi-Agents:');
console.log('- Gemini: Analyse web → videos');
console.log('- GPT-4o: Extraction PDF → catalogue');
console.log('- Claude: Orchestration + Site web\n');
