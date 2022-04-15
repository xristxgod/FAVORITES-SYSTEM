import asyncio

from flask import Blueprint, redirect, render_template, request, flash, url_for

from src import db
from src.service import FavoritesUsers
from src.forms import ClearAllFavoritesForm, SelectAllFavoritesForm
from config import logger

app = Blueprint("main", __name__)
favorites = FavoritesUsers()

@app.route("/", methods=["GET", "POST"])
def favorites_page():
    form_clear = ClearAllFavoritesForm()
    form_select = SelectAllFavoritesForm()
    try:
        if form_clear.submit_clear.data and form_clear.validate():
            favorites.clear_favorites_users()
            flash("All users have been added to favorites!", category="danger")
            return redirect(url_for("main.favorites_page"))
        if form_select.submit_select.data and form_select.validate():
            favorites.select_all_users()
            flash("All users have been added to favorites!", category="success")
            return redirect(url_for("main.favorites_page"))
    except Exception as error:
        logger.error(f"ERROR STEP 18: {error}")
        flash("Something went wrong!", category="danger")
        return redirect(url_for("main.favorites_page"))

    form_user_id = request.form.get('user_id')
    if form_user_id is not None:
        favorites.change_to_favorites(user_id=int(form_user_id))
        return redirect(url_for("main.favorites_page"))

    users = asyncio.run(db.get_users())
    favorites_users = []
    for user in users:
        if len(favorites.get_user_favorite) > 0:
            if favorites.is_in_favorites(user_id=user["id"]):
                favorites_users.append(
                    {"id": user["id"], "username": user["username"], "is_favorite": True}
                )
            else:
                favorites_users.append(
                    {"id": user["id"], "username": user["username"], "is_favorite": False}
                )
        else:
            favorites_users.append(
                {"id": user["id"], "username": user["username"], "is_favorite": False}
            )

    return render_template(
        "favorites.html",
        favorites_users_a=favorites_users,
        form_clear=form_clear,
        form_select=form_select,
    )