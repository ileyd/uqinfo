"""
Catalogue scraper
"""
import re
import helpers as helpers
from typing import List


class Catalogue:
  # list of all program IDs
  programs: List[int] = []

  def __init__(self):
    self.programs = []
    self.update()

  def update(self):
    """Updates self based on information scraped from UQ
    """
    base_url: str = 'https://www.uq.edu.au/study/browse.html?level=ugpg'
    soup = helpers.get_soup(base_url)

    programs = soup.find_all("a", href=re.compile("acad_prog"))
    for program in programs:
      program_code = program['href'][-4:]
      self.programs.append(program_code)
