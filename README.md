# docassemble.us

A [docassemble] extension that provides helper functions specific to
the United States.

The built-in **docassemble** functions [`states_list()`] and
[`state_name()`] are based on the ISO 3166-2 standard. For the United
States, that standard covers the 50 states, the District of Columbia,
and the territories, but it does not include everything that can
appear in the "state" part of a U.S. mailing address. An interview
that asks for an address using `states_list()` cannot accept the
address of a servicemember with an APO, FPO, or DPO address, for
example.

This package provides two functions, `us_states_list()` and
`us_state_name()`, that work like `states_list()` and `state_name()`
but are based on the two-letter abbreviations used by the U.S. Postal
Service. They cover:

* The 50 states
* The District of Columbia (`DC`)
* The territories: American Samoa (`AS`), Guam (`GU`), the Northern
  Mariana Islands (`MP`), Puerto Rico (`PR`), and the Virgin Islands
  (`VI`)
* The "states" used for military and diplomatic mail: Armed Forces
  Americas (`AA`), Armed Forces Europe (`AE`), and Armed Forces
  Pacific (`AP`)
* The freely associated states, which are served by the U.S. Postal
  Service: the Federated States of Micronesia (`FM`), the Marshall
  Islands (`MH`), and Palau (`PW`)

The list does not include the United States Minor Outlying Islands
(`UM`), which is part of the ISO standard but is not a USPS
abbreviation.

## Installation

Install the `docassemble.us` package on your server using [Package
Management].

## Usage

To make the functions available in an interview, include the module
in a [`modules`] block:

```yaml
modules:
  - docassemble.us.functions
```

### us_states_list()

`us_states_list()` returns a dictionary in which the keys are USPS
abbreviations and the values are names, sorted by name. It can be
used with [`code`] to populate the choices of a multiple-choice field:

```yaml
question: |
  What is your address?
fields:
  - Address: user.address.address
  - Unit: user.address.unit
    required: False
  - City: user.address.city
  - State: user.address.state
    code: |
      us_states_list()
  - Zip: user.address.zip
```

The variable `user.address.state` will be set to the abbreviation
(e.g., `'PA'`), and the user will see the name (e.g., `Pennsylvania`).

If you call `us_states_list(abbreviate=True)`, the values of the
dictionary will be the abbreviations instead of the names, so that
the user chooses from a list of abbreviations.

Unlike `states_list()`, `us_states_list()` does not accept a
`country_code` parameter.

### us_state_name()

`us_state_name()` returns the name that goes with a USPS
abbreviation.

```yaml
question: |
  You live in ${ us_state_name(user.address.state) }.
```

* `us_state_name('PA')` returns `'Pennsylvania'`.
* `us_state_name('AE')` returns `'Armed Forces Europe'`.

If the abbreviation is not recognized, the function returns the
abbreviation itself.

Unlike `state_name()`, `us_state_name()` does not accept a
`country_code` parameter.

### Translation

The names returned by both functions are passed through the
[`word()`] function, so they can be translated into other languages
using the **docassemble** [`words`] system.

[docassemble]: https://docassemble.org
[`states_list()`]: https://docassemble.org/docs/functions.html#states_list
[`state_name()`]: https://docassemble.org/docs/functions.html#state_name
[`word()`]: https://docassemble.org/docs/functions.html#word
[`words`]: https://docassemble.org/docs/config.html#words
[`modules`]: https://docassemble.org/docs/initial.html#modules
[`code`]: https://docassemble.org/docs/fields.html#code
[Package Management]: https://docassemble.org/docs/packages.html
