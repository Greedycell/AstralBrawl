from Protocol.Messages.Client.Account.ClientHelloMessage import ClientHelloMessage
from Protocol.Messages.Client.Account.LoginMessage import LoginMessage
from Protocol.Messages.Client.Account.ClientCapabilitiesMessage import ClientCapabilitiesMessage
from Protocol.Messages.Client.Account.KeepAliveMessage import KeepAliveMessage
from Protocol.Messages.Client.Home.AnalyticEventMessage import AnalyticEventMessage
from Protocol.Messages.Client.Home.SetDeviceTokenMessage import SetDeviceTokenMessage
from Protocol.Messages.Client.Home.ChangeAvatarNameMessage import ChangeAvatarNameMessage
from Protocol.Messages.Client.Social.AskForPlayingFacebookFriendsMessage import AskForPlayingFacebookFriendsMessage
from Protocol.Messages.Client.Home.EndClientTurnMessage import EndClientTurnMessage
from Protocol.Messages.Client.Home.StartMatchmakingMessage import StartMatchmakingMessage
from Protocol.Messages.Client.Home.CancelMatchmakingMessage import CancelMatchmakingMessage
from Protocol.Messages.Client.Home.GoHomeFromOfflinePracticeMessage import GoHomeFromOfflinePracticeMessage
from Protocol.Messages.Client.Home.AskForBattleEndMessage import AskForBattleEndMessage
from Protocol.Messages.Client.Home.GetPlayerProfileMessage import GetPlayerProfileMessage
from Protocol.Messages.Client.Home.HomeBattleReplayMessage import HomeBattleReplayMessage
from Protocol.Messages.Client.Alliance.AskForAllianceDataMessage import AskForAllianceDataMessage
from Protocol.Messages.Client.Alliance.AskForJoinableAlliancesListMessage import AskForJoinableAlliancesListMessage
from Protocol.Messages.Client.Team.TeamCreateMessage import TeamCreateMessage
from Protocol.Messages.Client.Team.TeamLeaveMessage import TeamLeaveMessage
from Protocol.Messages.Client.Team.TeamChangeMemberSettingsMessage import TeamChangeMemberSettingsMessage
from Protocol.Messages.Client.Team.TeamSetMemberReadyMessage import TeamSetMemberReadyMessage
from Protocol.Messages.Client.Team.TeamSetRankedLocationMessage import TeamSetRankedLocationMessage
from Protocol.Messages.Client.Team.TeamSetLocationMessage import TeamSetLocationMessage
from Protocol.Messages.Client.Home.PlayerStatusMessage import PlayerStatusMessage
from Protocol.Messages.Client.Home.GetLeaderboardMessage import GetLeaderboardMessage

MessageFactory = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10107: ClientCapabilitiesMessage,
    10108: KeepAliveMessage,
    10110: AnalyticEventMessage,
    10113: SetDeviceTokenMessage,
    10212: ChangeAvatarNameMessage,
    10513: AskForPlayingFacebookFriendsMessage,
    14102: EndClientTurnMessage,
    14103: StartMatchmakingMessage,
    14106: CancelMatchmakingMessage,
    14109: GoHomeFromOfflinePracticeMessage,
    14110: AskForBattleEndMessage,
    14113: GetPlayerProfileMessage,
    14114: HomeBattleReplayMessage,
    14302: AskForAllianceDataMessage,
    14303: AskForJoinableAlliancesListMessage,
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14354: TeamChangeMemberSettingsMessage,
    14355: TeamSetMemberReadyMessage,
    14361: StartMatchmakingMessage,
    14362: TeamSetRankedLocationMessage,
    14363: TeamSetLocationMessage,
    14366: PlayerStatusMessage,
    14403: GetLeaderboardMessage
}