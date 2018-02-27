"""
Catalogue scraper
"""
import re
import helpers as helpers

class Catalogue:
    programs: list = []
    url: str = 'https://www.uq.edu.au/study/browse.html?level=ugpg'

def catalogue():
    """
    Scrapes list of programs identified by title and program code
    :return: List object, containing dictionaries of program details
    """
    program_list = []
    # selection filter (program_code)
    program_selection_filter = ['2030', '2342']

    url = 'https://www.uq.edu.au/study/browse.html?level=ugpg'
    soup = helpers.get_soup(url)

    raw_programs = soup.find_all('a', href=re.compile("acad_prog"))
    for raw_program in raw_programs:
        program_code = raw_program['href'][-4:]
        program_list.append(program_code)

    return program_list