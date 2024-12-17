from enum import Enum
from typing import List

class AvailableSeason:
    def __init__(self, year: int, display_season: str) -> None:
        self.year = year
        self.display_season = display_season


class Country(Enum):
    EMPTY = ""
    UNITED_STATES = "United States"


class CountryFlag(Enum):
    EMPTY = ""
    USA = "USA"


class PlayerPlayer:
    def __init__(self, id: str, first_name: str, last_name: str, short_name: str, display_name: str, abbreviations: str, abbreviations_accessibility_text: str, amateur: bool, country: Country, country_flag: CountryFlag, line_color: str, seed, status, tour_bound, assets) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.short_name = short_name
        self.display_name = display_name
        self.abbreviations = abbreviations
        self.abbreviations_accessibility_text = abbreviations_accessibility_text
        self.amateur = amateur
        self.country = country
        self.country_flag = country_flag
        self.line_color = line_color
        self.seed = seed
        self.status = status
        self.tour_bound = tour_bound
        self.assets = assets


class Round:
    def __init__(self, score: str, par_relative_score: str) -> None:
        self.score = score
        self.par_relative_score = par_relative_score


class PlayerElement:
    def __init__(self, id: str, position: str, player: PlayerPlayer, rounds: List[Round], additional_data: List[str], total: str, par_relative_score: str) -> None:
        self.id = id
        self.position = position
        self.player = player
        self.rounds = rounds
        self.additional_data = additional_data
        self.total = total
        self.par_relative_score = par_relative_score


class Winner:
    def __init__(self, id: str, first_name: str, last_name: str, total_strokes: int, total_score: int, country_flag: CountryFlag, country_name: Country, purse, display_points: bool, display_purse: bool, points, seed: str, points_label, winner_icon) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.total_strokes = total_strokes
        self.total_score = total_score
        self.country_flag = country_flag
        self.country_name = country_name
        self.purse = purse
        self.display_points = display_points
        self.display_purse = display_purse
        self.points = points
        self.seed = seed
        self.points_label = points_label
        self.winner_icon = winner_icon


class TournamentPastResults:
    def __init__(self, id: str, players: List[PlayerElement], teams, rounds: List[str], additional_data_headers: List[str], available_seasons: List[AvailableSeason], winner: Winner, winning_team, recap) -> None:
        self.id = id
        self.players = players
        self.teams = teams
        self.rounds = rounds
        self.additional_data_headers = additional_data_headers
        self.available_seasons = available_seasons
        self.winner = winner
        self.winning_team = winning_team
        self.recap = recap