from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json
import models

app = Flask(__name__)
app.secret_key = 'secret_key_for_demo'\
    

# ========================
# Routes côté Utilisateur
# ========================

@app.route('/')
def user_home():
    matches = models.load_matches()
    live = [m for m in matches if m.get('status') == 'live']
    return render_template('user_home.html', matches=live)

@app.route('/live')
def live_matches():
    matches = models.load_matches()
    live = [m for m in matches if m.get('status') == 'live']
    return render_template('live_matches.html', matches=live)

@app.route('/upcoming')
def upcoming_matches():
    matches = models.load_matches()
    upcoming = [m for m in matches if m.get('status') == 'upcoming']
    return render_template('upcoming_matches.html', matches=upcoming)

@app.route('/history')
def match_history():
    matches = models.load_matches()
    history = [m for m in matches if m.get('status') == 'finished']
    return render_template('match_history.html', matches=history)

@app.route('/ranking')
def ranking():
    players = models.load_players()
    sorted_players = sorted(players, key=lambda x: x.get('points', 0), reverse=True)
    return render_template('ranking.html', players=sorted_players)

# =====================
# Routes côté Admin
# =====================

@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

# Gestion des matchs
@app.route('/admin/matches')
def admin_matches():
    matches = models.load_matches()
    return render_template('admin_matches.html', matches=matches)

@app.route('/admin/matches/create', methods=['GET', 'POST'])
def create_match():
    if request.method == 'POST':
        matches = models.load_matches()
        new_id = max([m['id'] for m in matches], default=0) + 1
        new_match = {
            'id': new_id,
            'team_a': request.form['team_a'],
            'team_b': request.form['team_b'],
            'date': request.form['date'],
            'status': request.form['status']  # 'upcoming', 'live' ou 'finished'
        }
        # Si le match est terminé, il faut enregistrer le score et le meilleur joueur
        if new_match['status'] == 'finished':
            try:
                new_match['score_team_a'] = int(request.form.get('score_team_a', 0))
                new_match['score_team_b'] = int(request.form.get('score_team_b', 0))
            except ValueError:
                new_match['score_team_a'] = 0
                new_match['score_team_b'] = 0
            new_match['best_player'] = request.form['best_player']
        matches.append(new_match)
        models.save_matches(matches)
        flash('Match créé avec succès!', 'success')
        return redirect(url_for('admin_matches'))
    return render_template('admin_edit_match.html', match=None)

@app.route('/admin/matches/edit/<int:match_id>', methods=['GET', 'POST'])
def edit_match(match_id):
    matches = models.load_matches()
    match = next((m for m in matches if m['id'] == match_id), None)
    if not match:
        flash('Match non trouvé.', 'danger')
        return redirect(url_for('admin_matches'))
    if request.method == 'POST':
        match['team_a'] = request.form['team_a']
        match['team_b'] = request.form['team_b']
        match['date'] = request.form['date']
        match['status'] = request.form['status']
        if match['status'] == 'finished':
            try:
                match['score_team_a'] = int(request.form.get('score_team_a', 0))
                match['score_team_b'] = int(request.form.get('score_team_b', 0))
            except ValueError:
                match['score_team_a'] = 0
                match['score_team_b'] = 0
            match['best_player'] = request.form['best_player']
        else:
            # Suppression des champs spécifiques aux matchs terminés si le statut n'est plus 'finished'
            match.pop('score_team_a', None)
            match.pop('score_team_b', None)
            match.pop('best_player', None)
        models.save_matches(matches)
        flash('Match mis à jour!', 'success')
        return redirect(url_for('admin_matches'))
    return render_template('admin_edit_match.html', match=match)

@app.route('/admin/matches/delete/<int:match_id>', methods=['POST'])
def delete_match(match_id):
    matches = models.load_matches()
    matches = [m for m in matches if m['id'] != match_id]
    models.save_matches(matches)
    flash('Match supprimé.', 'success')
    return redirect(url_for('admin_matches'))

# Gestion des joueurs
@app.route('/admin/players')
def admin_players():
    players = models.load_players()
    return render_template('admin_players.html', players=players)

@app.route('/admin/players/create', methods=['GET', 'POST'])
def create_player():
    if request.method == 'POST':
        players = models.load_players()
        new_id = max([p['id'] for p in players], default=0) + 1
        new_player = {
            'id': new_id,
            'name': request.form['name'],
            'position': request.form['position'],
            'points': int(request.form.get('points', 0)),
            'team': request.form['team']
        }
        players.append(new_player)
        models.save_players(players)
        flash('Joueur créé avec succès!', 'success')
        return redirect(url_for('admin_players'))
    return render_template('admin_edit_player.html', player=None)

@app.route('/admin/players/edit/<int:player_id>', methods=['GET', 'POST'])
def edit_player(player_id):
    players = models.load_players()
    player = next((p for p in players if p['id'] == player_id), None)
    if not player:
        flash('Joueur non trouvé.', 'danger')
        return redirect(url_for('admin_players'))
    if request.method == 'POST':
        player['name'] = request.form['name']
        player['position'] = request.form['position']
        player['points'] = int(request.form.get('points', 0))
        player['team'] = request.form['team']
        models.save_players(players)
        flash('Joueur mis à jour!', 'success')
        return redirect(url_for('admin_players'))
    return render_template('admin_edit_player.html', player=player)

@app.route('/admin/players/delete/<int:player_id>', methods=['POST'])
def delete_player(player_id):
    players = models.load_players()
    players = [p for p in players if p['id'] != player_id]
    models.save_players(players)
    flash('Joueur supprimé.', 'success')
    return redirect(url_for('admin_players'))

# Initialisation des fichiers de données si nécessaire
if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    if not os.path.exists(os.path.join('data', 'players.json')):
        with open(os.path.join('data', 'players.json'), 'w') as f:
            json.dump([], f)
    if not os.path.exists(os.path.join('data', 'matches.json')):
        with open(os.path.join('data', 'matches.json'), 'w') as f:
            json.dump([], f)
    app.run(debug=True)
