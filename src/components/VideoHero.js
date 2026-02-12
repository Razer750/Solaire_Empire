/**
 * VideoHero.js - Composant Hero avec Vidéos Projets
 * Intègre les liens analysés par Gemini depuis advsolarpower.com
 *
 * Architecture Multi-Agents:
 * - Données source: agents/results_gemini_web.json
 * - Analysé par: Gemini (via OpenRouter)
 * - Intégré par: Claude Sonnet 4.5
 */

import React, { useState, useEffect } from 'react';
import './VideoHero.css';

const VideoHero = () => {
  const [videos, setVideos] = useState([]);
  const [branding, setBranding] = useState(null);
  const [activeVideo, setActiveVideo] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadVideoData();
  }, []);

  /**
   * Charge les données vidéos depuis results_gemini_web.json
   */
  const loadVideoData = async () => {
    try {
      const response = await fetch('../agents/results_gemini_web.json');
      const data = await response.json();

      // Extraction des données Gemini
      const geminiResults = Array.isArray(data.results)
        ? data.results[0]
        : data.results;

      setVideos(geminiResults.videos || []);
      setBranding(geminiResults.branding || {});

      // Active la première vidéo par défaut
      if (geminiResults.videos?.length > 0) {
        setActiveVideo(geminiResults.videos[0]);
      }

      setLoading(false);
      console.log('✓ VideoHero: Données Gemini chargées', {
        videos: geminiResults.videos?.length,
        slogans: geminiResults.branding?.slogans?.length
      });
    } catch (error) {
      console.error('Erreur chargement VideoHero:', error);
      setLoading(false);
      // Fallback avec données exemple
      loadFallbackData();
    }
  };

  /**
   * Données de secours si Gemini non disponible
   */
  const loadFallbackData = () => {
    setVideos([
      {
        url: "https://youtube.com/watch?v=example_cdte",
        titre: "Révolution CdTe en Action",
        type: "reel",
        duree: "60s"
      }
    ]);
    setBranding({
      slogans: ["La Révolution CdTe", "Moins cher • Plus beau • Stock France"],
      arguments_vente: ["Prix -30%", "Esthétique premium", "Stock Ivry"]
    });
  };

  /**
   * Extrait l'ID YouTube d'une URL
   */
  const getYouTubeId = (url) => {
    const match = url?.match(/(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&?]+)/);
    return match ? match[1] : null;
  };

  /**
   * Gère le changement de vidéo active
   */
  const handleVideoChange = (video) => {
    setActiveVideo(video);
  };

  if (loading) {
    return (
      <div className="video-hero loading">
        <div className="spinner"></div>
        <p>Chargement des projets...</p>
      </div>
    );
  }

  return (
    <section className="video-hero">
      {/* Hero Header */}
      <div className="hero-header">
        <h1 className="hero-title glitch" data-text="RÉVOLUTION CdTe">
          RÉVOLUTION CdTe
        </h1>

        {/* Slogans rotatifs */}
        {branding?.slogans && (
          <div className="hero-slogans">
            {branding.slogans.map((slogan, idx) => (
              <span key={idx} className="slogan" style={{animationDelay: `${idx * 2}s`}}>
                {slogan}
              </span>
            ))}
          </div>
        )}

        {/* Arguments de vente */}
        {branding?.arguments_vente && (
          <div className="hero-arguments">
            {branding.arguments_vente.slice(0, 3).map((arg, idx) => (
              <div key={idx} className="argument-badge">
                <span className="badge-icon">✓</span>
                {arg}
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Vidéo principale */}
      {activeVideo && (
        <div className="main-video-container">
          <div className="video-wrapper">
            {getYouTubeId(activeVideo.url) ? (
              <iframe
                className="video-player"
                src={`https://www.youtube.com/embed/${getYouTubeId(activeVideo.url)}?autoplay=1&mute=1&loop=1&playlist=${getYouTubeId(activeVideo.url)}`}
                title={activeVideo.titre}
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              ></iframe>
            ) : (
              <div className="video-placeholder">
                <div className="placeholder-icon">▶️</div>
                <p>{activeVideo.titre}</p>
              </div>
            )}
          </div>

          <div className="video-info">
            <span className="video-type-badge">{activeVideo.type}</span>
            <h3 className="video-title">{activeVideo.titre}</h3>
            {activeVideo.duree && (
              <span className="video-duration">⏱ {activeVideo.duree}</span>
            )}
          </div>
        </div>
      )}

      {/* Playlist vidéos */}
      {videos.length > 1 && (
        <div className="video-playlist">
          <h3 className="playlist-title">Nos Projets</h3>
          <div className="playlist-grid">
            {videos.map((video, idx) => (
              <div
                key={idx}
                className={`playlist-item ${activeVideo?.url === video.url ? 'active' : ''}`}
                onClick={() => handleVideoChange(video)}
              >
                <div className="playlist-thumbnail">
                  {getYouTubeId(video.url) ? (
                    <img
                      src={`https://img.youtube.com/vi/${getYouTubeId(video.url)}/mqdefault.jpg`}
                      alt={video.titre}
                    />
                  ) : (
                    <div className="thumbnail-placeholder">
                      {video.type === 'reel' ? '🎬' : video.type === 'demo' ? '🔧' : '📚'}
                    </div>
                  )}
                  <div className="play-overlay">▶</div>
                </div>
                <div className="playlist-item-info">
                  <p className="playlist-item-title">{video.titre}</p>
                  <span className="playlist-item-type">{video.type}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* CTA Section */}
      <div className="hero-cta-section">
        <h2>Prêt à Rejoindre la Révolution ?</h2>
        <p>Stock permanent à Ivry-sur-Seine (94) • Livraison Express 48h</p>
        <div className="cta-buttons">
          <a href="#catalogue" className="cta-button primary">
            Voir le Catalogue
          </a>
          <a href="#contact" className="cta-button secondary">
            Demander un Devis
          </a>
        </div>
      </div>

      {/* Métadonnées (SEO) */}
      <div className="hero-metadata" style={{display: 'none'}}>
        <span itemProp="name">Solaire Empire - Panneaux CdTe</span>
        <span itemProp="description">
          Panneaux solaires CdTe Honstar/Longyan. -30% moins cher,
          meilleur en faible lumière, stock France à Ivry.
        </span>
      </div>
    </section>
  );
};

export default VideoHero;
