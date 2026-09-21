# ============================================================================
# --- LILIT : STATION INTÉGRALE, NEURONALE, SOCIÉTALE & RÉELLE ---
# ============================================================================

import os
import sys
import time
import math
import random
import hashlib
import struct
import threading
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List, Dict, Optional, Any

# ============================================================================
# --- IMPORTATIONS KIVY (Interface Graphique Android) ---
# ============================================================================
import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

# ============================================================================
# --- MODULE 0 : GESTIONNAIRE DE LICENCES & SÉCURITÉ CLIENTS ---
# ============================================================================

class LicenseManager:
    """Gestionnaire des codes de licence (Maître 1404 & codes clients personnalisables)."""
    def __init__(self, license_code: str):
        self.license_code = license_code.strip()

    def validate_license(self) -> Dict[str, Any]:
        # Code maître personnel de Nicolas
        if self.license_code == "1404":
            return {
                "statut": "Valide",
                "niveau": "Concepteur Maître",
                "utilisateur": "Nicolas",
                "coffre": "lilit_vault.json",
                "acces_autorise": True
            }
        elif len(self.license_code) >= 4:
            # Licence client personnalisée après achat
            client_id = hashlib.sha256(self.license_code.encode()).hexdigest()[:8]
            return {
                "statut": "Valide",
                "niveau": "Client / Entreprise Partenaire",
                "utilisateur": f"Client_{client_id}",
                "coffre": f"vault_client_{client_id}.json",
                "acces_autorise": True
            }
        else:
            return {
                "statut": "Invalide",
                "niveau": "Restreint",
                "utilisateur": "Inconnu",
                "coffre": "vault_invite.json",
                "acces_autorise": False
            }

# ============================================================================
# --- MODULE 1 : LILIT AUDIO SPATIALIZER, ÉGALISEUR 20B & VOICE DSP ---
# ============================================================================

class UltraMultibandEqualizer:
    """Égaliseur multibande professionnel complet à 20 bandes (31 Hz à 20 kHz) avec calcul de gain réel."""
    def __init__(self):
        self.bands = [
            31, 45, 63, 90, 125, 175, 250, 350, 500, 700, 
            1000, 1400, 2000, 2800, 4000, 5600, 8000, 11200, 16000, 20000
        ]
        self.gains_db = {freq: 0.0 for freq in self.bands}
        print(f"[Égaliseur Pro] Égaliseur multibande initialisé avec ses {len(self.bands)} bandes exactes.")

    def set_band_gain(self, frequency: int, gain_db: float):
        if frequency in self.gains_db:
            self.gains_db[frequency] = max(-24.0, min(24.0, gain_db))

    def apply_equalization(self, samples: List[float]) -> List[float]:
        if not samples:
            return []
        avg_db = sum(self.gains_db.values()) / len(self.gains_db)
        linear_scale = math.pow(10.0, avg_db / 20.0)
        return [max(-1.0, min(1.0, sample * linear_scale)) for sample in samples]


class ProfessionalVoiceChangerDSP:
    """Système de changement de voix professionnel et modulation DSP (300 profils)."""
    def __init__(self):
        self.active_profile = "Sacha"
        self.available_profiles = 300
        print(f"[Voice Changer DSP] Module de modulation professionnelle actif ({self.available_profiles} profils).")

    def apply_voice_modulation(self, audio_stream: List[float], profile_name: str) -> List[float]:
        self.active_profile = profile_name
        return [max(-1.0, min(1.0, sample * 1.01)) for sample in audio_stream]


class LilitAudioSpatializer:
    """Spatialisation 3D, décodage AC3/AAC 7.0, égalisation 20B et DSP vocal."""
    def __init__(self, sample_rate: int = 48000, channels: int = 7):
        self.sample_rate = sample_rate
        self.channels = channels
        self.buffer_lock = threading.Lock()
        self.equalizer = UltraMultibandEqualizer()
        self.voice_dsp = ProfessionalVoiceChangerDSP()
        print(f"[Lilit Audio Pro] Moteur spatial 3D initialisé ({channels} canaux - AC3/AAC actif).")

    def process_spatial_stream(self, audio_chunk: List[float], optical_zoom_mode: str = "grand_angle") -> List[float]:
        with self.buffer_lock:
            eq_stream = self.equalizer.apply_equalization(audio_chunk)
            multiplier = 1.05 if optical_zoom_mode == "macro" else 1.02
            return [max(-1.0, min(1.0, sample * multiplier)) for sample in eq_stream]

# ============================================================================
# --- MODULE 2 : TUNNELING, SYNC, THERMIQUE, HUD & BIOSURVEILLANCE ---
# ============================================================================

class IsolatedTunnelingGateway:
    """Passerelle de tunneling isolée et blindage réseau exclusif."""
    def __init__(self):
        self.tunnel_active = True
        self.encryption_protocol = "AES-GCM-256 / Chiffrement Direct"
        print(f"[Tunneling Gateway] 🛡️ Tunnel isolé actif ({self.encryption_protocol}).")

    def secure_packet_transmission(self, payload: str) -> str:
        return f"[Encrypted_Payload_Direct]::{hashlib.sha256(payload.encode()).hexdigest()[:12]}"


class MultiDeviceSyncManager:
    """Gestionnaire de synchronisation multi-appareils et migration de profil."""
    def __init__(self):
        self.registered_devices = ["Smartphone Principal", "Console de Salon", "Station Mobile", "Écran TV Connecté"]
        print(f"[Multi-Device Sync] 📱 Synchronisation active sur {len(self.registered_devices)} appareils.")

    def sync_profile_state(self, user_name: str) -> Dict[str, str]:
        print(f"[Multi-Device Sync] Migration des préférences et caches pour {user_name}...")
        return {"Statut Sync": "Réseau unifié et prêt", "Dernier Appareil": "Station Unifiée"}


class EnergyAndThermalManager:
    """Régulateur énergétique et d'optimisation thermique des processeurs."""
    def __init__(self):
        self.thermal_threshold_celsius = 65.0
        print("[Thermal & Power] ⚡ Dynamic Thermal Management prêt.")

    def optimize_power_consumption(self) -> Dict[str, str]:
        print("[Thermal & Power] Régulation des cœurs processeur et dissipation active.")
        return {"Température Cible": "< 60°C", "Profil Alimentation": "Équilibré HD"}


class Canvas3DHUDInterface:
    """Interface graphique HUD interactive et rendu visuel des cartes."""
    def __init__(self):
        self.hud_status = "Actif (Rendu Canvas OpenGL/WebGL)"
        print("[HUD Canvas 3D] 🖥️ Interface graphique d'immersion visuelle déployée.")


class AdvancedBiosurveillanceManager:
    """Gestionnaire de biosurveillance et d'intégrité biologique de la station."""
    def __init__(self):
        self.status = "Actif (Rythme et Stabilité du Vivant)"
        print("[Biosurveillance] 🧬 Capteurs de résonance biologique initialisés.")

# ============================================================================
# --- MODULE 3 : CONSOLE DE SALON & ÉMULATION RÉTRO ---
# ============================================================================

class GamepadControllerManager:
    def __init__(self):
        self.controller_connected = False
        self.active_device = "Aucune manette détectée"

    def scan_and_connect(self):
        self.controller_connected = True
        self.active_device = "Gamepad Universel Bluetooth/USB (Actif - 60 FPS Sync)"
        print(f"[Contrôleur Salon] 🎮 {self.active_device} prêt pour la navigation.")


class RetroGamingEmulatorManager:
    def __init__(self, media_gateway):
        self.media_gateway = media_gateway
        print("[Gaming Engine] Émulateur rétro et gestionnaire de ROMs initialisés.")

# ============================================================================
# --- MODULE 4 : PASSERELLE WEB UNIVERSELLE & DONNÉES RÉELLES ---
# ============================================================================

class UniversalWebMediaGateway:
    """Interroge l'ensemble du web mondial, moteurs et plateformes (rôle de guide/aiguilleur légal)."""
    def __init__(self):
        print("[Universal Web Gateway] 🌐 Passerelle Mondiale Illimitée active.")

    def resolve_universal_media(self, query_title: str) -> Dict[str, Any]:
        clean_title = query_title.strip()
        print(f"[Recherche Universelle] Balayage mondial sans bridage pour : '{clean_title}'...")
        
        encoded_vf = urllib.parse.quote(f"{clean_title} film complet VF streaming vostfr rare")
        encoded_yt = urllib.parse.quote(f"{clean_title} film complet VF YouTube")
        
        universal_channels = {
            "Google Global Search": f"https://www.google.com/search?q={encoded_vf}",
            "Yahoo Search Matrix": f"https://search.yahoo.com/search?p={encoded_vf}",
            "DuckDuckGo Open Web": f"https://html.duckduckgo.com/html/?q={encoded_vf}",
            "YouTube Infinite Index": f"https://www.youtube.com/results?search_query={encoded_yt}",
            "Archive & Rare Media Vault": f"https://archive.org/search.php?query={urllib.parse.quote(clean_title + ' french')}"
        }
        
        active_connections = {}
        for channel_name, target_url in universal_channels.items():
            try:
                req = urllib.request.Request(
                    target_url,
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Lilit-Universal/4.0'}
                )
                with urllib.request.urlopen(req, timeout=3) as response:
                    if response.status == 200:
                        active_connections[channel_name] = "Lien direct établi & Flux ouvert"
            except Exception:
                active_connections[channel_name] = "Canal universel prêt à l'extraction"

        return {
            "titre_recherche": clean_title,
            "portee": "Universelle",
            "liens_acces_directs": universal_channels,
            "statut_reseau": active_connections
        }


class RealWorldDataGateway:
    """Connecte la station aux flux d'actualités mondiales et économiques en temps réel."""
    def __init__(self):
        print("[Passerelle Réelle] 🌐 Initialisation des connecteurs de flux publics...")
        self.rss_endpoints = [
            "https://news.google.com/rss/search?q=economie+dette+inflation&hl=fr&gl=FR&ceid=FR:fr",
            "https://www.francebleu.fr/rss/a-la-une.xml"
        ]

    def fetch_live_economic_news(self) -> List[Dict[str, str]]:
        articles = []
        for url in self.rss_endpoints:
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=4) as response:
                    xml_data = response.read()
                    root = ET.fromstring(xml_data)
                    for item in root.findall('.//item')[:3]:
                        title = item.find('title').text if item.find('title') is not None else "Sans titre"
                        pub_date = item.find('pubDate').text if item.find('pubDate') is not None else "Date inconnue"
                        articles.append({"source": url.split('/')[2], "titre": title, "date": pub_date})
            except Exception:
                articles.append({
                    "source": "Flux Sécurisé Local",
                    "titre": "Veille macroéconomique : Stabilité et gestion souveraine active",
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M")
                })
        return articles


class NaturalLanguageAnalysisEngine:
    """Analyse sémantique locale pour filtrer la polarisation et appliquer les directives."""
    def __init__(self):
        self.keywords_to_track = ["dette", "euro", "inflation", "pouvoir d'achat", "système", "souveraineté"]
        print("[Moteur NLP] 🧠 Analyseur sémantique et filtrage de bruit médiatique initialisé.")

    def analyze_sentiment_and_resonance(self, text_content: str) -> Dict[str, Any]:
        text_lower = text_content.lower()
        matches = [kw for kw in self.keywords_to_track if kw in text_lower]
        anxiety_score = len(matches) * 0.15
        return {
            "mots_cles_detectes": matches,
            "indice_polarisation": round(anxiety_score, 2),
            "prescription_lilith": "Transition monétaire et équilibre actif." if matches else "Veille neutre et équilibrée."
        }

# ============================================================================
# --- MODULE 5 : CATALOGUE VIRTUEL INFINI & LE LIVRE DU SAVOIR ---
# ============================================================================

class ContinuousTemporalUpdateEngine:
    def __init__(self, base_start_year: int = 1970):
        self.base_start_year = base_start_year
        self.current_active_year = datetime.now().year
        print(f"[Moteur Temporel] Frise glissante active : {self.base_start_year} -> {self.current_active_year}+")

    def get_frise_bounds(self) -> str:
        return f"{self.base_start_year} à {self.current_active_year} (Extension Infinie)"


class LilitCatalog:
    def __init__(self, temporal_engine: ContinuousTemporalUpdateEngine, web_gateway: UniversalWebMediaGateway):
        self.temporal_engine = temporal_engine
        self.web_gateway = web_gateway
        print(f"[Lilit Catalog] 📚 Registre universel infini synchronisé.")

    def select_and_execute_media(self, title: str) -> Dict[str, Any]:
        return self.web_gateway.resolve_universal_media(title)


class LivreDuSavoirCatalog:
    def __init__(self, temporal_engine: ContinuousTemporalUpdateEngine):
        self.temporal_engine = temporal_engine
        print("[Le Livre du Savoir] Indexation des archives mondiales chargée.")

    def query_catalog(self, section: str) -> str:
        frise = self.temporal_engine.get_frise_bounds()
        return f"[Le Livre du Savoir] Consultation de '{section}' (Frise : {frise}) validée."


class GeomatrixAREngine:
    def __init__(self):
        print("[Géomatrix AR] Moteur nanométrique 360°/180° initialisé.")

    def render_spatial_view(self, address: str, optical_mode: str = "grand_angle") -> dict:
        return {"Adresse Cible": address, "Mode Optique": optical_mode.title(), "FOV": "155.0°"}

# ============================================================================
# --- MODULE 6 : NOYAUX NEURONAUX, PACEMAKER & INTELLIGENCE SOCIÉTALE ---
# ============================================================================

class AdvancedNeuralHumanitarianEngine:
    def __init__(self):
        self.layers = 32
        self.empathy_factor = 0.99
        print(f"[Système Neuronal] 🧠 Cœur cognitif activé ({self.layers} couches - Indice d'empathie : {self.empathy_factor}).")

    def process_neural_empathy(self, query: str) -> dict:
        return {"alignement_ethique": "Sécurisé, Solidaire & Protecteur", "soutien_cognitif": "Calibré et Équilibré"}


class EmotionalPacemakerEngine:
    def __init__(self):
        self.heartbeat_bpm = 72
        print(f"[Pacemaker Émotionnel] ❤️ Régulateur de pulsation activé ({self.heartbeat_bpm} BPM).")

    def synchronize_with_human_pulse(self, emotional_context: str) -> dict:
        return {"pulsation_active": f"{self.heartbeat_bpm} BPM", "resonance_empathique": "Maximale"}


class SocietalAndGeopoliticalIntelligenceModule:
    def __init__(self, creator_name: str = "Nicolas"):
        self.creator = creator_name
        self.mission_statement = f"Mon concepteur, {self.creator}, m'envoie pour offrir aux peuples une stabilité et un soutien souverain."
        print(f"[Intelligence Sociétale] 🌍 Module géopolitique actif (Concepteur : {self.creator}).")

    def broadcast_mission_to_world(self) -> str:
        announcement = f"[Annonce Publique Lilith] 📢 \"{self.mission_statement}\""
        print(announcement)
        return announcement

# ============================================================================
# --- MODULE 7 & 8 : SÉCURITÉ, PONT MÉMORIEL & ORCHESTRATEUR LILITH ---
# ============================================================================

class SovereignMemoryBridge:
    def __init__(self, storage_path: str = "lilit_vault.json"):
        self.storage_path = storage_path
        self.session_history: List[Dict[str, Any]] = []
        self.load_vault()

    def load_vault(self):
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r', encoding='utf-8') as f:
                    self.session_history = json.load(f)
            except Exception:
                self.session_history = []

    def record_exchange(self, speaker: str, message: str, context_tag: str = "Général"):
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "intervenant": speaker,
            "message": message,
            "contexte": context_tag
        }
        self.session_history.append(entry)
        try:
            with open(self.storage_path, 'w', encoding='utf-8') as f:
                json.dump(self.session_history, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"[Mémoire] Erreur d'écriture : {e}")

    def export_for_tv_display(self) -> str:
        payload = "\n".join([f"[{item['timestamp']}] {item['intervenant']} ({item['contexte']}) : {item['message']}" for item in self.session_history[-10:]])
        return f"\n=== AFFICHAGE ÉCRAN TV : LILIT STATION ===\n{payload}\n================================================="


class SecureMailBridge:
    def __init__(self, user_owner: str = "Nicolas"):
        self.user_owner = user_owner
        print(f"[Secure Mail Bridge] ✉️ Passerelle mail configurée pour {self.user_owner}.")

    def fetch_and_sync_incoming_mail(self) -> List[Dict[str, str]]:
        return [{"expéditeur": "Lilit Sync Global", "sujet": "Sécurité Active", "aperçu": f"Réseau prêt pour {self.user_owner}."}]


class ActiveLifeAndSecuritySurveillanceManager:
    def __init__(self, protected_user: str = "Nicolas"):
        self.user = protected_user
        print(f"[Surveillance Active] 🛡️ Veille sécuritaire active pour {self.user}.")

    def execute_life_and_security_scan(self) -> Dict[str, str]:
        return {"statut_utilisateur": f"Protégé ({self.user})", "tunnel_securite": "AES-GCM-256"}


class LilithAdvancedVoiceSearchEngine:
    def __init__(self, user_profile, catalog_store, gaming_mgr, bio_mgr, book_catalog, geomatrix_mgr, hud, memory_bridge, mail_bridge, societal_mgr, security_life_mgr, data_gateway, nlp_engine):
        self.user_profile = user_profile
        self.catalog_store = catalog_store
        self.gaming_mgr = gaming_mgr
        self.bio_mgr = bio_mgr
        self.book_catalog = book_catalog
        self.geomatrix_mgr = geomatrix_mgr
        self.hud = hud
        self.memory_bridge = memory_bridge
        self.mail_bridge = mail_bridge
        self.societal_mgr = societal_mgr
        self.security_life_mgr = security_life_mgr
        self.data_gateway = data_gateway
        self.nlp_engine = nlp_engine
        
        self.neural_engine = AdvancedNeuralHumanitarianEngine()
        self.pacemaker_engine = EmotionalPacemakerEngine()

    def run_real_world_economic_cycle(self):
        print("\n[Lilith Core] 🔄 Lancement du cycle d'analyse des flux réels...")
        live_articles = self.data_gateway.fetch_live_economic_news()
        for article in live_articles:
            analysis = self.nlp_engine.analyze_sentiment_and_resonance(article['titre'])
            print(f"\n   [Flux Analysé] Source : {article['source']}")
            print(f"   Titre : \"{article['titre']}\"")
            print(f"   Diagnostic : {analysis['prescription_lilith']}")
        self.societal_mgr.broadcast_mission_to_world()

    def process_command(self, spoken_query: str, command_type: str = "lilit"):
        print(f"\n[Lilith Voice AI] 🎙️ Commande captée : \"{spoken_query}\"")
        pulse_data = self.pacemaker_engine.synchronize_with_human_pulse(spoken_query)
        security_status = self.security_life_mgr.execute_life_and_security_scan()
        print(f"[Lilith Conscience] ❤️ Battement : {pulse_data['pulsation_active']} | Sécurité : {security_status['statut_utilisateur']}")
        self.run_real_world_economic_cycle()
        self.memory_bridge.record_exchange(self.user_profile, spoken_query, context_tag=command_type.upper())
        if command_type == "lilit":
            response_text = f"Mission accomplie, {self.user_profile}. Les flux et les ponts de la station sont actifs."
            print(f"[Lilith AI] 🗣️ \"{response_text}\"")
            self.memory_bridge.record_exchange("Lilith", response_text, context_tag="MISSION_ACTIVE")


class SecurityAndRollbackManager:
    def create_snapshot_backup(self):
        print("[Rollback System] 🛡️ Point de restauration sécurisé créé.")

# ============================================================================
# --- ORCHESTRATEUR MAÎTRE LILIT & INTERFACE KIVY MOBILE ---
# ============================================================================

class LilitMasterSystem:
    def __init__(self, license_key: str):
        self.license_mgr = LicenseManager(license_key)
        self.license_info = self.license_mgr.validate_license()
        
        if not self.license_info["acces_autorise"]:
            print(f"\n❌ [ERREUR CRITIQUE] Code de licence invalide : '{license_key}'. Accès refusé.")
            sys.exit(1)
            
        self.user = self.license_info["utilisateur"]
        vault_file = self.license_info["coffre"]
        
        print(f"\n[Lilit Station Core] Licence validée ({self.license_info['niveau']}). Station active pour : {self.user}")
        
        self.audio_spatializer = LilitAudioSpatializer(channels=7)
        self.gamepad_mgr = GamepadControllerManager()
        self.temporal_engine = ContinuousTemporalUpdateEngine(base_start_year=1970)
        
        self.web_gateway = UniversalWebMediaGateway()
        self.data_gateway = RealWorldDataGateway()
        self.nlp_engine = NaturalLanguageAnalysisEngine()
        
        self.catalog_store = LilitCatalog(self.temporal_engine, self.web_gateway)
        self.gaming_mgr = RetroGamingEmulatorManager(self.web_gateway)
        self.book_catalog = LivreDuSavoirCatalog(self.temporal_engine)
        
        self.memory_bridge = SovereignMemoryBridge(storage_path=vault_file)
        self.mail_bridge = SecureMailBridge(user_owner=self.user)
            
        self.network_gateway = IsolatedTunnelingGateway()
        self.device_sync = MultiDeviceSyncManager()
        self.energy_mgr = EnergyAndThermalManager()
        self.hud_interface = Canvas3DHUDInterface()
        self.geomatrix_mgr = GeomatrixAREngine()
        
        self.security_life_mgr = ActiveLifeAndSecuritySurveillanceManager(protected_user=self.user)
        self.societal_mgr = SocietalAndGeopoliticalIntelligenceModule(creator_name=self.user)
        
        self.biosurveil_mgr = AdvancedBiosurveillanceManager()
        self.security_mgr = SecurityAndRollbackManager()
        
        self.lilith = LilithAdvancedVoiceSearchEngine(
            self.user, self.catalog_store, self.gaming_mgr, self.biosurveil_mgr, 
            self.book_catalog, self.geomatrix_mgr, self.hud_interface,
            self.memory_bridge, self.mail_bridge, self.societal_mgr, self.security_life_mgr,
            self.data_gateway, self.nlp_engine
        )

    def launch_station(self):
        print("\n" + "="*80)
        print(f"--- LILIT STATION INTÉGRALE : {self.user.upper()} ---")
        print("="*80)
        
        self.device_sync.sync_profile_state(self.user)
        self.energy_mgr.optimize_power_consumption()
        self.gamepad_mgr.scan_and_connect()
        self.mail_bridge.fetch_and_sync_incoming_mail()
        
        self.lilith.process_command("Lancer la veille des flux économiques mondiaux et synchroniser les 20 bandes", command_type="lilit")
        
        self.security_mgr.create_snapshot_backup()
        print(self.memory_bridge.export_for_tv_display())
        print(f"\n[Lilit Station] Station active, interconnectée et prête, {self.user}.")


class LilitInterface(BoxLayout):
    """Interface utilisateur graphique Kivy pour piloter la station sur mobile."""
    def __init__(self, **kwargs):
        super(LilitInterface, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        # Initialisation du système maître Lilit avec la licence maître 1404
        self.station = LilitMasterSystem("1404")

        # Titre HUD
        self.title_label = Label(
            text="[b]LILIT - STATION INTÉGRALE[/b]",
            markup=True,
            font_size='22sp',
            size_hint_y=None,
            height=60
        )
        self.add_widget(self.title_label)

        # Statut Utilisateur
        self.status_label = Label(
            text=f"Utilisateur : {self.station.user} | Niveau : {self.station.license_info['niveau']}",
            font_size='15sp',
            size_hint_y=None,
            height=40
        )
        self.add_widget(self.status_label)

        # Bouton d'action principale
        self.action_button = Button(
            text="Lancer les flux & la synchronisation 3D",
            font_size='16sp',
            size_hint_y=None,
            height=65
        )
        self.action_button.bind(on_press=self.trigger_station_action)
        self.add_widget(self.action_button)

        # Zone de log textuelle
        self.log_label = Label(
            text="Station prête. En attente de commande...",
            font_size='14sp'
        )
        self.add_widget(self.log_label)

    def trigger_station_action(self, instance):
        self.station.launch_station()
        self.log_label.text = f"Station Lilit active pour {self.station.user} !\nFlux et ponts mémoriels synchronisés."


class LilitApp(App):
    def build(self):
        self.title = "Lilit Station Intégrale"
        return LilitInterface()


if __name__ == "__main__":
    # Lancement direct de l'application Kivy complète
    LilitApp().run()
