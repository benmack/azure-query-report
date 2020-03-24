from IPython.display import display, Markdown, HTML
import pandas as pd
import warnings

class ReportItem:

    _description_separator = "<div><b>=================<br></b></div><div><b>INTERNAL DETAILS<br></b></div><div><b>=================</b></div>"

    def __init__(self, item: pd.Series, report_internals=False):
        """Create an item to be reported.
        
        Parameters
        ----------
        item : pd.Series
            Report item containing at least the columns:
                * Title
                * Description
                * Acceptance Criteria
                
        Returns
        -------
        ReportItem
            Object with useful reporting methods.
        """
        self._item = item
        self._report_internals = report_internals
        self._details_heading_level = 3

    def display_separator(self):
        heading = "#" * self._details_heading_level
        display(Markdown(f'{heading} {self._item.Title}'))

    def display_details_header(self):
        heading = "#" * self._details_heading_level
        display(Markdown(f'{heading} {self._item.Title}'))

    def display_description_header(self):
        heading = "#" * (self._details_heading_level + 1)
        display(Markdown(f'{heading} Description'))

    def display_acceptance_criteria_header(self):
        heading = "#" * (self._details_heading_level + 1)
        display(Markdown(f'{heading} Acceptance Criteria'))

    def display_description(self):
        description = self.get_description()
        display(HTML(description))

    def display_acceptance_criteria(self):
        display(HTML(self._item["Acceptance Criteria"]))

    def display_separtion_line(self):
        display(Markdown('---'))

    def get_description(self):
        if self._report_internals:
            description = self._item.Description
        else:
            if self._description_separator not in self._item.Description:
                warnings.warn("description separator not found in description")
            description = self._item.Description.split(self._description_separator)[0]
        return description

    @staticmethod
    def got_to_overview():
        go_to_overview = '<a href="#OVERVIEW">Back to OVERVIEW</a>'
        display(HTML(go_to_overview))

def get_clickable_items(items, columns_overview):
    make_clickable = TitleToClickableConverter(items.Title.values)
    overview = items[columns_overview].astype(str).style.format(make_clickable)
    return overview

class TitleToClickableConverter:
    def __init__(self, titles):
        self._titles = titles
    def make_clickable(self, val):
        if val in self._titles:
            link = "#" + val.replace(" ", "-")
            return '<a href="{}">{}</a>'.format(link , val)
        else:
            return val
    def __call__(self, val):
        return self.make_clickable(val)