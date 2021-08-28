# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class PrecisionInput(Component):
    """A PrecisionInput component.
A numeric input component that converts
an input value to the desired precision.

Keyword arguments:

- id (string; optional):
    The ID used to identify this compnent in Dash callbacks.

- className (string; optional):
    Class to apply to the root component element.

- disabled (boolean; optional):
    If True, numeric input cannot be changed.

- label (dict; optional):
    Description to be displayed alongside the scientific notation. To
    control styling,  pass an object with label and style properties.

    `label` is a string | dict with keys:

    - label (string; optional)

    - style (dict; optional)

- labelPosition (a value equal to: 'top', 'bottom'; default 'top'):
    Where the numeric input label is positioned.

- max (number; default Number.MAX_SAFE_INTEGER):
    The maximum value of the numeric input.

- min (number; default 0):
    The minimum value of the numeric input.

- persisted_props (list of a value equal to: 'value's; default ['value']):
    Properties whose user interactions will persist after refreshing
    the  component or the page. Since only `value` is allowed this
    prop can  normally be ignored.

- persistence (boolean | string | number; optional):
    Used to allow user interactions in this component to be persisted
    when  the component - or the page - is refreshed. If `persisted`
    is truthy and  hasn't changed from its previous value, a `value`
    that the user has  changed while using the app will keep that
    change, as long as  the new `value` also matches what was given
    originally.  Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Where persisted user changes will be stored:  memory: only kept in
    memory, reset on page refresh.  local: window.localStorage, data
    is kept after the browser quit.  session: window.sessionStorage,
    data is cleared once the browser quit.

- precision (number; default 2):
    Number of significant figures.

- size (number; optional):
    The size (length) of the numeric input in pixels.

- style (dict; optional):
    Style to apply to the root component element.

- theme (dict; default light):
    Theme configuration to be set by a ThemeProvider.

- value (number; optional):
    The value of numeric input."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, value=Component.UNDEFINED, size=Component.UNDEFINED, min=Component.UNDEFINED, max=Component.UNDEFINED, precision=Component.UNDEFINED, disabled=Component.UNDEFINED, theme=Component.UNDEFINED, label=Component.UNDEFINED, labelPosition=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'disabled', 'label', 'labelPosition', 'max', 'min', 'persisted_props', 'persistence', 'persistence_type', 'precision', 'size', 'style', 'theme', 'value']
        self._type = 'PrecisionInput'
        self._namespace = 'dash_daq'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'disabled', 'label', 'labelPosition', 'max', 'min', 'persisted_props', 'persistence', 'persistence_type', 'precision', 'size', 'style', 'theme', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(PrecisionInput, self).__init__(**args)
