"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask, render_template

def create_app():

    APP = Flask(__name__)

    @APP.route('/')
    def root():
    
        return 'OpenAQ Air Quality Dashboard'

    return APP