#!/usr/bin/python
# -*- coding:utf-8 -*-

#how to run:
#export flask_app=app    <-name of the py file
#export FLASK_ENV=development
#flask run

import flask
import os
import sqlite3
import json
import datetime




app=flask.Flask(__name__)
app.config['SECRET_KEY'] = "ccc60394]@%dsfpjzpZPFJPDC122é"
#flask.session["language"]="en"

@app.route("/")
def index():

	if flask.request.method=="GET":
		if "language" in flask.request.values:
			flask.session["language"]=flask.request.values["language"]
	if not "language" in flask.session:
		flask.session["language"]="en"
	
	return flask.render_template("index.html",current_page="index")

@app.route("/index.html")
def index_copy():
	if flask.request.method=="GET":
		if "language" in flask.request.values:
			flask.session["language"]=flask.request.values["language"]
	if not "language" in flask.session:
		flask.session["language"]="en"
	
	return flask.render_template("index.html",current_page="index")

@app.route("/publications.html")
def page_publi():
	if flask.request.method=="GET":
		if "language" in flask.request.values:
			flask.session["language"]=flask.request.values["language"]
	if not "language" in flask.session:
		flask.session["language"]="en"
	return flask.render_template("publi.html",current_page="publications")


@app.route("/thesis.html")
def page_thesis():
	if flask.request.method=="GET":
		if "language" in flask.request.values:
			flask.session["language"]=flask.request.values["language"]
	if not "language" in flask.session:
		flask.session["language"]="en"
	return flask.render_template("thesis.html",current_page="thesis")

@app.route("/more.html")
def page_more():
	if flask.request.method=="GET":
		if "language" in flask.request.values:
			flask.session["language"]=flask.request.values["language"]
	if not "language" in flask.session:
		flask.session["language"]="en"
	return flask.render_template("more.html",current_page="more")
