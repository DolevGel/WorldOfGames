import random
import yfinance as yf
import logging


def get_money_interval(difficulty, total_value):
    logging.debug("Retrieving exchange rate from Yahoo Finance...")
    ticker = yf.Ticker("USDILS=X")
    history = ticker.history(period="1m")
    exchange_rate = history["Close"].iloc[-1]
    lower_bound = total_value - (5 - difficulty)
    upper_bound = total_value + (5 - difficulty)
    return lower_bound * exchange_rate, upper_bound * exchange_rate


def get_guess_from_user():
    while True:
        try:
            guess = float(input("Enter your guess for the value in ILS: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def play_currency_roulette(difficulty):
    total_value = random.randint(1, 100)
    interval = get_money_interval(difficulty, total_value)
    print(f"Guess the value of this USD amount in ILS - {total_value}$:")
    guess = get_guess_from_user()
    return interval[0] <= guess <= interval[1]
