import json
from flask import Flask, render_template, request, redirect, flash, url_for
import datetime


def load_clubs():
    """
    Load all clubs saved in the file "clubs.json".
    :return: list of clubs where each club is saved with a dictionary
    """
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    """
        Load all competitions saved in the file "competitions.json"
        :return: list of competitions where each competition is saved with a dictionary
        """
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


app = Flask(__name__)
app.secret_key = 'something_special'

clubs = load_clubs()
competitions = load_competitions()


@app.route('/')
def index():
    """Display the page of connexion"""
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    """
    Display the page with a list of available competitions.
    For each competition, a button allows user to book places
    If the client is not connected, the client is redirected on index.html.
    :return: template
    """
    for each_club in clubs:
        if request.form['email'] == each_club['email']:
            club = each_club
            return render_template('welcome.html', club=club, competitions=competitions)
        else:
            return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    competition_date = transform_string_in_datetime(found_competition['date'])
    if found_club and found_competition:
        if competition_date[0] < competition_date[1]:
            flash("This competition is finished, you can't book places")
            return render_template("welcome.html", club=club, competitions=competitions)
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    """
    Display the list of competitions after booking places with the template "welcome.html"
    :return: template
    """
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
    club['points'] = int(club['points']) - places_required
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


def transform_string_in_datetime(string_date):
    competition_date, competition_hour = string_date.split()
    competition_date_str = competition_date.split("-")
    competition_hour_str = competition_hour.split(":")
    competition_date = datetime.datetime(int(competition_date_str[0]),
                                         int(competition_date_str[1]),
                                         int(competition_date_str[2]),
                                         int(competition_hour_str[0]),
                                         int(competition_hour_str[1]),
                                         int(competition_hour_str[2]))
    today_datetime = datetime.datetime.now()
    return competition_date, today_datetime
