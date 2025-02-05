import pwnagotchi.plugins as plugins
import logging

class AutoForgetLost(plugins.Plugin):
    __author__ = 'c0d3-5t3w'
    __version__ = '1.0.0'
    __license__ = 'MIT'
    __description__ = "For use when travling to fast to keep up with clients. Will remove clients that are out of range. (further than -200dBm)"
    
    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger(__name__)

    def on_loaded(self):
        self._logger.info("AutoForgetLost plugin loaded.")

    def on_unloaded(self):
        self._logger.info("AutoForgetLost plugin unloaded.")

    def on_ai_ready(self, agent):
        self._logger.info("AI is ready, checking for lost clients.")
        self._remove_lost_clients(agent)

    def on_ai_step(self, agent, step):
        self._logger.info("AI step, checking for lost clients.")
        self._remove_lost_clients(agent)

    def _remove_lost_clients(self, agent):
        lost_clients = []
        for client in agent.known_clients():
            if not self._is_client_in_range(client):
                lost_clients.append(client)
        
        for client in lost_clients:
            self._logger.info(f"Removing lost client: {client['mac']}")
            agent.forget_client(client['mac'])

    def _is_client_in_range(self, client):
        return client['signal'] > -200

