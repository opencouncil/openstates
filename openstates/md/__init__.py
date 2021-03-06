import datetime
from billy.utils.fulltext import pdfdata_to_text, text_after_line_numbers

metadata = dict(
    name='Maryland',
    abbreviation='md',
    capitol_timezone='America/New_York',
    legislature_name='Maryland General Assembly',
    chambers = {
        'upper': {'name': 'Senate', 'title': 'Senator'},
        'lower': {'name': 'House', 'title': 'Delegate'},
    },
    terms=[
        {'name': '2007-2010', 'sessions': ['2007', '2007s1', '2008',
                                           '2009', '2010'],
         'start_year': 2007, 'end_year': 2010},
        {'name': '2011-2014', 'sessions': ['2011', '2011s1', '2012',
                                           '2012s1', '2012s2', '2013'],
         'start_year': 2011, 'end_year': 2014},
    ],
    session_details={
        '2007': {'start_date': datetime.date(2007,1,10),
                 'end_date': datetime.date(2007,4,10),
                 'number': 423,
                 'display_name': '2007 Regular Session',
                 'type': 'primary',
                 '_scraped_name': '2007 Regular Session',
                },
        '2007s1': {'start_date': datetime.date(2007,10,29),
                   'end_date': datetime.date(2007,11,19),
                   'display_name': '2007, 1st Special Session',
                   'number': 424,
                   'type': 'special',
                   '_scraped_name': '2007 Special Session 1',
                  },
        '2008': {'start_date': datetime.date(2008,1,9),
                 'end_date': datetime.date(2008,4,7),
                 'display_name': '2008 Regular Session',
                 'number': 425,
                 'type': 'primary',
                 '_scraped_name': '2008 Regular Session',
                },
        '2009': {'start_date': datetime.date(2009,1,14),
                 'end_date': datetime.date(2009,4,13),
                 'display_name': '2009 Regular Session',
                 'number': 426,
                 'type': 'primary',
                 '_scraped_name': '2009 Regular Session',
                },
        '2010': {'start_date': datetime.date(2010,1,13),
                 'end_date': datetime.date(2010,4,12),
                 'number': 427,
                 'display_name': '2010 Regular Session',
                 'type': 'primary',
                 '_scraped_name': '2010 Regular Session',
                },
        '2011': {'start_date': datetime.date(2011,1,12),
                 'end_date': datetime.date(2011,4,12),
                 'number': 428,
                 'display_name': '2011 Regular Session',
                 'type': 'primary',
                 '_scraped_name': '2011 Regular Session',
                },
        '2011s1': {'number': 429,
                   'display_name': '2011, 1st Special Session',
                   'type': 'special',
                   '_scraped_name': '2011 Special Session 1',
                  },
        '2012': {'start_date': datetime.date(2012,1,11),
                 'end_date': datetime.date(2012,4,9),
                 'number': 430,
                 'display_name': '2012 Regular Session',
                 'type': 'primary',
                 '_scraped_name': '2012 Regular Session',
                },
        '2012s1': {'number': 431,
                   'display_name': '2012, 1st Special Session',
                   'type': 'special',
                   '_scraped_name': '2012 Special Session 1',
                  },
        '2012s2': {'display_name': '2012, 2nd Special Session',
                   'type': 'special',
                   '_scraped_name': '2012 Special Session 2',
                  },
        '2013': {'display_name': '2013 Regular Session',
                   'type': 'special',
                   '_scraped_name': '2013 Regular Session',
                  },
    },
    feature_flags=['subjects', 'events', 'influenceexplorer'],
    _ignored_scraped_sessions=['1996 Regular Session',
                               '1997 Regular Session',
                               '1998 Regular Session',
                               '1999 Regular Session',
                               '2000 Regular Session',
                               '2001 Regular Session',
                               '2002 Regular Session',
                               '2003 Regular Session',
                               '2004 Regular Session',
                               '2004 Special Session 1',
                               '2005 Regular Session',
                               '2006 Regular Session',
                               '2006 Special Session 1']
)


def session_list():
    from billy.scrape.utils import url_xpath
    return url_xpath('http://mgaleg.maryland.gov/webmga/frmLegislation.aspx?pid=legisnpage&tab=subject3',
                     '//select[contains(@name, "cboSession")]/option/text()')


def extract_text(doc, data):
    text = pdfdata_to_text(data)
    return text_after_line_numbers(text)
