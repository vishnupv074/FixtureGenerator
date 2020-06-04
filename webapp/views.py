from django.shortcuts import render, redirect
from .models import Teams, Matches, Venues
from datetime import date, timedelta
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Login view for admin login
def login_view(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            msg = 'Invalid Credentials'
        else:
            login(request, user)
            return redirect('admin_panel')
    return render(request, 'login.html', {'msg': msg})


def logout_view(request):
    logout(request)
    return redirect('schedule')


# Entry to admin panel it requires login
@login_required(login_url='login')
def admin_panel(request):
    msg = ''
    matches = ''
    try:
        matches = Matches.objects.all()
    except:
        msg = " Schedule not generated "
    return render(request, 'admin_panel.html', {'matches': matches, 'msg': msg})


# View for editing match only for logged in user
@login_required(login_url='login')
def match_edit(request, id=None):
    msg =''
    match = ''
    if request.method == 'POST':
        id = request.POST.get('match_id')
        match = Matches.objects.get(id=id)
        match.team1_score = request.POST.get('team1_score')
        match.team2_score = request.POST.get('team2_score')
        if request.POST.get('is_completed') == 'on':
            match.match_over = True
        else:
            match.match_over = False
        match.save()  # Saving updated scores and match status

    if id is None:
        return redirect('admin_panel')
    else:
        try:
            match = Matches.objects.get(id=id)  # getting match object with given id
        except:
            msg = 'Object not exist'

    return render(request, 'match_edit.html', {'msg': msg, 'match': match})


# View for registering the teams
def registartion(request):

    start_date = date(2020, 1, 7)
    teams = Teams.objects.all()
    if len(teams) < 10:
        if request.method == 'POST':
            new_team = Teams()
            new_team.teamName = request.POST.get('team_name')
            new_team.manager = request.POST.get('manager')
            new_team.coach = request.POST.get('coach')
            new_team.player1 = request.POST.get('player1')
            new_team.player2 = request.POST.get('player2')
            new_team.player3 = request.POST.get('player3')
            new_team.player4 = request.POST.get('player4')
            new_team.player5 = request.POST.get('player5')
            new_team.player6 = request.POST.get('player6')
            new_team.player7 = request.POST.get('player7')
            new_team.player8 = request.POST.get('player8')
            new_team.player9 = request.POST.get('player9')
            new_team.player10 = request.POST.get('player10')
            new_team.player11 = request.POST.get('player11')
            new_team.save()

            if len(Teams.objects.all()) == 10:  # Checks whether the number of teams is 10
                ts = Teams.objects.all()
                teams = [i.id for i in ts]  # Getting list of ids of Team objects

                def comb(players):  # Function for making combinations by using round robin
                    """ Create a schedule for the players in the list and return it"""
                    s = []
                    if len(players) % 2 == 1: players = players + [None]
                    n = len(players)
                    map = list(range(n))
                    mid = n // 2
                    for i in range(n - 1):
                        l1 = map[:mid]
                        l2 = map[mid:]
                        l2.reverse()
                        round = []
                        for j in range(mid):
                            t1 = players[l1[j]]
                            t2 = players[l2[j]]
                            if j == 0 and i % 2 == 1:
                                round.append((t2, t1))
                            else:
                                round.append((t1, t2))
                        s.append(round)
                        map = map[mid:-1] + map[:mid] + map[-1:]
                    return s

                schedule = comb(teams)  # Calling the function for making combination and stored in schedule
                for i in range(len(schedule)):  # Performing actions for arranging the combination
                    schedule[i][-2], schedule[i][-1] = schedule[i][-1], schedule[i][-2]
                venue = Venues.objects.all()
                next_date = start_date
                for l in schedule:  # Taking each collection of combinations
                    k = l
                    while len(k) != 0:
                        if len(k) != 1:
                            t1, t2 = k.pop(0)
                            match = Matches()  # Creating and updating the Fixture objects
                            match.date = next_date
                            match.team1 = Teams.objects.get(id=t1)
                            match.team2 = Teams.objects.get(id=t2)
                            match.venue = random.choice(venue)  # Randomly setting a venue
                            match.save()

                            t1, t2 = k.pop(0)
                            match = Matches()
                            match.date = next_date
                            match.team1 = Teams.objects.get(id=t1)
                            match.team2 = Teams.objects.get(id=t2)
                            match.venue = random.choice(venue)
                            match.save()
                            next_date += timedelta(1)  # Incrementing 1 day after scheduling 2 games for the day
                        else:
                            t1, t2 = k.pop(0)
                            match = Matches()
                            match.date = next_date
                            match.team1 = Teams.objects.get(id=t1)
                            match.team2 = Teams.objects.get(id=t2)
                            match.venue = random.choice(venue)
                            match.save()
                            next_date += timedelta(1)

                    next_date += timedelta(1)  # Taking a gap after a round

                return redirect('schedule')

            else:
                return redirect('team_view', new_team.id)  # For viewing the team just registered

    else:
        return redirect('schedule')
    return render(request, 'registration.html', {})


# View for viewing the team and their fixture
def team_view(request, id=None):  # View for viewing a team and their fixtures
    team = ''
    msg = ''
    fixtures = ''
    if id:
        team = Teams.objects.get(id=id)

    if len(Teams.objects.all()) == 10:
        fixtures = Matches.objects.filter(Q(team1=id) | Q(team2=id))

    return render(request, 'team.html', {'team': team, 'fixtures': fixtures})  # Passing the team and their fixture


# View for showing the complete fixture, completed games etc.
def schedule_view(request):
    if request.user.is_authenticated:
        return redirect('admin_panel')
    teams = Teams.objects.all()
    schedule = msg = ''

    if len(teams) < 10:
        msg = 'Schedule not generated'

    else:
        schedule = Matches.objects.all()
        teams = Teams.objects.all()

    return render(request, 'schedule.html', {'matches': schedule, 'msg': msg, 'teams': teams })
