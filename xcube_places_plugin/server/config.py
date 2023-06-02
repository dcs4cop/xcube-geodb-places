# The MIT License (MIT)
# Copyright (c) 2021/2022 by the xcube team and contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from xcube.util.jsonschema import JsonArraySchema
from xcube.util.jsonschema import JsonObjectSchema
from xcube.util.jsonschema import JsonStringSchema

GPLACES_CONFIG_SCHEMA = JsonObjectSchema(
    properties=dict(
        XcubePlaces=JsonObjectSchema(properties=dict(
            GeoDBConf=JsonObjectSchema(properties=dict(
                PostgrestUrl=JsonStringSchema(),
                PostgrestPort=JsonStringSchema(),
                ClientId=JsonStringSchema(),
                ClientSecret=JsonStringSchema(),
                AuthDomain=JsonStringSchema())
            ),
            PlaceGroups=JsonObjectSchema(properties=dict(
                Identifier=JsonStringSchema(min_length=1),
                Title=JsonStringSchema(),
                Query=JsonStringSchema())
            ),
            DatasetRefs=JsonArraySchema(),
            PropertyMapping=JsonObjectSchema(properties=dict(
                Label=JsonStringSchema(),
                Color=JsonStringSchema(),
                Description=JsonStringSchema()
            ))
        ))),
    additional_properties=True
)
