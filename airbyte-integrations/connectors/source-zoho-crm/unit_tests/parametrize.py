#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#

from collections import namedtuple

import pytest

TestCase = namedtuple("TestCase", ("json_type", "data_type", "length", "decimal_place", "api_name", "pick_list_values", "expected_values"))


datatype_inputs = pytest.mark.parametrize(
    TestCase._fields,
    (
        TestCase("boolean", "boolean", None, None, "Field", [], {"title": "Field", "type": ["null", "boolean"]}),
        TestCase("double", "double", None, 3, "Field", [], {"multipleOf": 0.001, "title": "Field", "type": ["null", "number"]}),
        TestCase("double", "currency", None, 2, "Field", [], {"multipleOf": 0.01, "title": "Field", "type": ["null", "number"]}),
        TestCase("integer", "integer", None, None, "Field", [], {"title": "Field", "type": ["null", "integer"]}),
        TestCase("string", "profileimage", 256, None, "Field", [], {"maxLength": 256, "title": "Field", "type": ["null", "string"]}),
        TestCase(
            "string",
            "picklist",
            128,
            None,
            "Field",
            ["Chelsea", "Arsenal", "ManUtd"],
            {"enum": [None, "Chelsea", "Arsenal", "ManUtd"], "maxLength": 128, "title": "Field", "type": ["null", "string"]},
        ),
        TestCase("string", "textarea", 1024, None, "Field", [], {"maxLength": 1024, "title": "Field", "type": ["null", "string"]}),
        TestCase(
            "string",
            "website",
            256,
            None,
            "Field",
            [],
            {
                "format": "uri",
                "maxLength": 256,
                "title": "Field",
                "type": ["null", "string"],
            },
        ),
        TestCase(
            "string",
            "date",
            16,
            None,
            "Field",
            [],
            {
                "format": "date",
                "maxLength": 16,
                "title": "Field",
                "type": ["null", "string"],
            },
        ),
        TestCase(
            "string",
            "datetime",
            32,
            None,
            "Field",
            [],
            {
                "format": "date-time",
                "maxLength": 32,
                "title": "Field",
                "type": ["null", "string"],
            },
        ),
        TestCase("string", "text", 1024, None, "Field", [], {"maxLength": 1024, "title": "Field", "type": ["null", "string"]}),
        TestCase("string", "phone", 16, None, "Field", [], {"maxLength": 16, "title": "Field", "type": ["null", "string"]}),
        TestCase(
            "string",
            "bigint",
            None,
            None,
            "Field",
            [],
            {
                "airbyte_type": "big_integer",
                "maxLength": None,
                "title": "Field",
                "type": ["null", "string"],
            },
        ),
        TestCase(
            "string",
            "event_reminder",
            None,
            None,
            "Reminder",
            ["15 min", "30 min", "1 hour"],
            {"format": "date-time", "title": "Reminder", "type": ["null", "string"]},
        ),
        TestCase(
            "string",
            "email",
            256,
            None,
            "Field",
            [],
            {
                "format": "email",
                "maxLength": 256,
                "title": "Field",
                "type": ["null", "string"],
            },
        ),
        TestCase(
            "string",
            "autonumber",
            512,
            None,
            "Field",
            [],
            {
                "airbyte_type": "big_integer",
                "maxLength": 512,
                "title": "Field",
                "type": ["null", "string"],
            },
        ),
        TestCase(
            "jsonobject",
            "ownerlookup",
            None,
            None,
            "Field",
            [],
            {
                "additionalProperties": False,
                "properties": {
                    "email": {"format": "email", "type": "string"},
                    "id": {"type": "string"},
                    "name": {"type": ["null", "string"]},
                },
                "required": ["name", "id", "email"],
                "title": "Field",
                "type": ["null", "object"],
            },
        ),
        TestCase("jsonobject", "RRULE", None, None, "Field", [], {"type": ["null", "object"]}),
        TestCase("jsonobject", "ALARM", None, None, "Field", [], {"type": ["null", "object"]}),
        TestCase(
            "jsonobject",
            "lookup",
            None,
            None,
            "Field",
            [],
            {
                "additionalProperties": False,
                "properties": {"id": {"type": "string"}, "name": {"type": ["null", "string"]}},
                "required": ["name", "id"],
                "title": "Field",
                "type": ["null", "object"],
            },
        ),
        TestCase(
            "jsonarray",
            "bigint",
            1024,
            None,
            "Field",
            [],
            {"items": {"airbyte_type": "big_integer", "type": "string"}, "title": "Field", "type": "array"},
        ),
        TestCase("jsonarray", "text", 2056, None, "Field", [], {"items": {"type": "string"}, "title": "Field", "type": "array"}),
        TestCase(
            "jsonarray",
            "text",
            2056,
            None,
            "Pricing_Details",
            [],
            {"items": {"type": "object"}, "title": "Pricing_Details", "type": "array"},
        ),
        TestCase(
            "jsonarray",
            "text",
            2056,
            None,
            "Product_Details",
            [],
            {"items": {"type": "object"}, "title": "Product_Details", "type": "array"},
        ),
        TestCase(
            "jsonarray",
            "string",
            None,
            None,
            "Tag",
            [],
            {
                "items": {
                    "additionalProperties": False,
                    "properties": {"id": {"type": "string"}, "name": {"type": "string"}},
                    "required": ["name", "id"],
                    "type": "object",
                },
                "title": "Tag",
                "type": "array",
            },
        ),
        TestCase(
            "jsonarray",
            "multiselectpicklist",
            128,
            None,
            "Field",
            ["A", "B", "C", "D"],
            {
                "items": {"enum": [None, "A", "B", "C", "D"], "type": ["null", "string"]},
                "minItems": 1,
                "title": "Field",
                "type": "array",
                "uniqueItems": True,
            },
        ),
    ),
)
