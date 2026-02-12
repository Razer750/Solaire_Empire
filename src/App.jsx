import React from 'react'
import VideoHero from './components/VideoHero.jsx'

function App() {
  return (
    <div className="App">
      <VideoHero />

      {/* Section Révolution CdTe */}
      <section id="revolution" className="section revolution-section">
        <h2>Pourquoi le CdTe ?</h2>
        <p className="section-intro">Le Telluride de Cadmium (CdTe) révolutionne le photovoltaïque</p>

        <div className="revolution-grid">
          <div className="revolution-card">
            <div className="card-icon">💰</div>
            <h3>Économique</h3>
            <p>Coût de production inférieur de 30%. Le CdTe démocratise l'énergie solaire.</p>
          </div>

          <div className="revolution-card">
            <div className="card-icon">🌙</div>
            <h3>Performant</h3>
            <p>Meilleur rendement en faible luminosité. Parfait pour le climat français.</p>
          </div>

          <div className="revolution-card">
            <div className="card-icon">🎨</div>
            <h3>Esthétique</h3>
            <p>Panneau noir uniforme premium. Design épuré et moderne.</p>
          </div>

          <div className="revolution-card">
            <div className="card-icon">🌍</div>
            <h3>Écologique</h3>
            <p>Impact environnemental réduit. Bilan carbone optimisé.</p>
          </div>
        </div>
      </section>

      {/* Section Contact */}
      <section id="contact" className="section contact-section">
        <h2>Prêt à Rejoindre la Révolution ?</h2>
        <p>Stock permanent à Ivry-sur-Seine (93) • Livraison Express • Support 7j/7</p>

        <form className="contact-form">
          <input type="text" placeholder="Nom" required />
          <input type="email" placeholder="Email" required />
          <input type="tel" placeholder="Téléphone" required />
          <select required>
            <option value="">Type de projet</option>
            <option value="particulier">Particulier (Maison)</option>
            <option value="professionnel">Professionnel (Entreprise)</option>
            <option value="installateur">Installateur (Partenaire)</option>
            <option value="investisseur">Investisseur (Centrale)</option>
          </select>
          <textarea placeholder="Message" rows="4"></textarea>
          <button type="submit" className="cta-button">Demander un devis</button>
        </form>
      </section>

      <footer>
        <p>&copy; 2025 Solaire Empire - La Révolution CdTe</p>
        <p>Stock France : Ivry-sur-Seine (93) • Certifications CE, TÜV</p>
      </footer>
    </div>
  )
}

export default App
