# Run application locally

Clone app

`git clone https://github.com/edmundcheng221/reviews-tracker-backend.git`

Navigate to the directory where the application.py and test_application.py files are:

`cd [path]`

Download dependencies

`pip3 install -r requirements.txt`

Run application using cli

`python application.py "https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183"`

# Sample JSON output

```

[
  {
    "title": "Great Company",
    "comment": "Was looking to find a positive solution for me to combine a loan and a credit card with higher interest to make one payment at a lower rate that I could payoff earlier than required.  First Midwest Bank was a great solu
tion for me and they were so professional and worked with me to achieve my needs. ",
    "author": "Sharon",
    "stars": "5",
    "date": "August 2021"
  },

  ...

  {
    "title": "I was a great experience!",
    "comment": "The process was simple and Margarita was very timely and helpful. Funded in 3 days. I would highly recommend! ",
    "author": "Michael",
    "stars": "5",
    "date": "July 2021"
  }
]

```

# Test

Run unit tests

`python3 test_application.py`