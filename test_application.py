import unittest
from application import LendingTreeParser


class TestLendingTreeParser(unittest.TestCase):

    # Check if each the lenth of titles, comments, etc are the same
    # Ensure that each title has a corresponding author and so forth
    def test_count(self):
        res = LendingTreeParser("https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183")
        title_len = len(res.get_reviews_title())
        comment_len = len(res.get_reviews_comment())
        author_len = len(res.get_reviews_author())
        star_len = len(res.get_reviews_num_stars())
        publish_len = len(res.get_reviews_publish_date())
        self.assertEqual(title_len,comment_len)
        self.assertEqual(comment_len,author_len)
        self.assertEqual(author_len,star_len)
        self.assertEqual(star_len,publish_len)

    # Check if the titles are correct
    def test_titles(self):
        res = LendingTreeParser("https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183")
        titles = res.get_reviews_title()
        self.assertEqual(titles, ['Great Company', 'Fantastic!!!', 'Great experience', 'Personal Loan', 'Excellent experience and customer service.', 'Good experience ', 'Very good experience ', 'Friendly and relaxing ', 'It was a great experience.', 'I was a great experience!'])

    # Check if comments are correct
    def test_comments(self):
        res = LendingTreeParser("https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183")
        comment3 = res.get_reviews_comment()[2]
        self.assertEqual(comment3, "The entire staff that I had conversations with were extremely professional but with a personal touch.  I will be giving this banking institution more if my business.")

    # Check if the authors are correct
    def test_author(self):
        res = LendingTreeParser("https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183")
        auth = res.get_reviews_author()
        print(auth)
        self.assertEqual(auth, ['Sharon', 'Ezra', 'Adeline', 'MaryAnn', 'Margaret', 'Daniel', 'Amanda', 'Kevin', 'Darlene', 'Michael'])

    # Check if the ratings are correct
    def test_star(self):
        res = LendingTreeParser("https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183")
        star = res.get_reviews_num_stars()
        print(star)
        self.assertEqual(star, ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5'])

    # Check if the publish dates are correct
    def test_publish(self):
        res = LendingTreeParser("https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183")
        publish = res.get_reviews_publish_date()
        print(publish)
        self.assertEqual(publish, ['August 2021', 'August 2021', 'August 2021', 'July 2021', 'July 2021', 'July 2021', 'July 2021', 'July 2021', 'July 2021', 'July 2021'])


if __name__ == '__main__':
    unittest.main()