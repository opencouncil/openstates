import datetime
from billy.utils.fulltext import pdfdata_to_text, text_after_line_numbers

metadata = dict(
    _partial_vote_bill_id=True,

    name='Rhode Island',
    abbreviation='ri',
    capitol_timezone='America/New_York',
    legislature_name='Rhode Island General Assembly',
    chambers = {
        'upper': {'name': 'Senate', 'title': 'Senator'},
        'lower': {'name': 'House', 'title': 'Representative'},
    },
    terms=[
        {'name': '2012',
         'start_year': 2012,
         'start_date': datetime.date(2012, 1, 4),
         'end_year': 2012,
         'sessions': ['2012']},
        {'name': '2013',
         'start_year': 2013,
         'end_year': 2014,
         'sessions': ['2013']},
    ],
    feature_flags=['subjects', 'events', 'influenceexplorer'],
    session_details={
        '2012': {'start_date': datetime.date(2012, 1, 4),
                 'type': 'primary',
                 'display_name': '2012 Regular Session'},
        '2013': {'type': 'primary',
                 'display_name': '2013 Regular Session'},
    },
    _ignored_scraped_sessions=['2013', '2012', '2011', '2010', '2009', '2008',
                               '2007']
)


def session_list():
    from billy.scrape.utils import url_xpath
    return url_xpath('http://status.rilin.state.ri.us/bill_history.aspx?mode=previous',
                     "//select[@name='ctl00$rilinContent$cbYear']/option/text()")


def extract_text(doc, data):
    return text_after_line_numbers(pdfdata_to_text(data))
