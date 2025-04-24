from typing import Type
from mautrix.client import InternalEventType, MembershipEventDispatcher, SyncStream
from mautrix.types import StateEvent, RoomID
from mautrix.util.config import BaseProxyConfig, ConfigUpdateHelper
from maubot import Plugin
from maubot.handlers import event


class Config(BaseProxyConfig):
    def do_update(self, helper: ConfigUpdateHelper) -> None:
        helper.copy("watch_room")
        helper.copy("welcome_message")
        helper.copy("notification_room")
        helper.copy("notification_message")


class GreetingsBot(Plugin):
    async def start(self) -> None:
        await super().start()
        self.config.load_and_update()
        self.client.add_dispatcher(MembershipEventDispatcher)
        self.log.info("GreetingsBot gestartet.")

    @event.on(InternalEventType.JOIN)
    async def on_join(self, evt: StateEvent) -> None:
        if not (evt.source & SyncStream.TIMELINE):
            return

        room_id = self.config["watch_room"]
        if evt.room_id != room_id:
            return

        user_link = f'<a href="https://matrix.to/#/{evt.sender}">{evt.sender}</a>'
        room_link = f'<a href="https://matrix.to/#/{evt.room_id}">{evt.room_id}</a>'

        # Willkommensnachricht senden
        welcome_msg = self.config["welcome_message"].format(user=user_link)
        await self.client.send_notice(evt.room_id, html=welcome_msg)

        # IT benachrichtigen
        notification_msg = self.config["notification_message"].format(
            user=user_link,
            room=room_link
        )
        notification_room = self.config["notification_room"]
        if notification_room:
            await self.client.send_notice(RoomID(notification_room), html=notification_msg)

    @classmethod
    def get_config_class(cls) -> Type[BaseProxyConfig]:
        return Config

    @staticmethod
    def default_config() -> dict:
        return {
            "watch_room": "!example:matrix.org",
            "welcome_message": "👋 Willkommen {user}!",
            "notification_room": "!admin:matrix.org",
            "notification_message": "📥 {user} ist dem Raum {room} beigetreten."
        }
