import us
from docassemble.base.functions import ensure_definition, word

__all__ = ['us_states_list', 'us_state_name']

# USPS abbreviations that are not part of the us package: the "states"
# used for military mail and the freely associated states.
ADDITIONAL_USPS_ABBREVIATIONS = {
    'AA': 'Armed Forces Americas',
    'AE': 'Armed Forces Europe',
    'AP': 'Armed Forces Pacific',
    'FM': 'Federated States of Micronesia',
    'MH': 'Marshall Islands',
    'PW': 'Palau'
}


def usps_abbreviations():
    mapping = {state.abbr: state.name for state in us.states.STATES_AND_TERRITORIES}
    # DC is only in STATES_AND_TERRITORIES if the DC_STATEHOOD
    # environment variable is set
    mapping[us.states.DC.abbr] = us.states.DC.name
    mapping.update(ADDITIONAL_USPS_ABBREVIATIONS)
    return mapping


def us_state_name(state_code):
    """Return the full name of a U.S. state, territory, or other USPS "state" given its abbreviation.

    Args:
        state_code (str): The USPS abbreviation (e.g., ``'NY'`` for New York).

    Returns:
        str: The full name, passed through ``word()`` for translation.
            Returns the original ``state_code`` if not found.
    """
    ensure_definition(state_code)
    mapping = usps_abbreviations()
    if state_code in mapping:
        return word(mapping[state_code])
    return state_code


def us_states_list(abbreviate=False):
    """Return a dictionary of USPS state abbreviations to full names.

    Includes the 50 states, the District of Columbia, the territories,
    the freely associated states, and the Armed Forces "states" used
    for military mail, sorted by name, suitable for use in a
    multiple-choice field.

    Args:
        abbreviate (bool, optional): If True, both keys and values will be the
            USPS abbreviation. Defaults to False.

    Returns:
        dict: A dictionary mapping USPS abbreviations to full names,
            or abbreviations to abbreviations if ``abbreviate=True``.
    """
    ensure_definition(abbreviate)
    mapping = {}
    for abbr, name in usps_abbreviations().items():
        if abbreviate:
            mapping[abbr] = abbr
        else:
            mapping[abbr] = word(name)
    return dict(sorted(mapping.items(), key=lambda item: item[1]))
