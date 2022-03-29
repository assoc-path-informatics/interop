Title: The OpenAPI Specification
Slug: openapi-post
Date: 2022-01-26
Category: Formats
Tags: openapi, interoperability
Authors: Steven Hart

## What is the OpenAPI specification and what does it mean to AI/ML in digital pathology?
The OpenAPI Specification (OAS) defines a standard, programming language-agnostic interface description for HTTP APIs,
which allows both humans and computers to discover and understand the capabilities of a service without requiring 
access to source code, additional documentation, or inspection of network traffic. When properly defined via OpenAPI, a
consumer can understand and interact with the remote service with a minimal amount of implementation logic. Similar to 
what interface descriptions have done for lower-level programming, the OpenAPI Specification removes guesswork in 
calling a service<sup> [1](https://spec.openapis.org/oas/v3.1.0) </sup>.

Digital Pathology is a constantly evolving space. There are numerous vendors and academics in this space trying to 
develop tools aimed at decreasing the monotony of repetitive tasks like cell counting to more complex survival/response
to therapy predictions. Needless to say, there is significantly more work to do in this space than any one person, 
institution, or even association could attempt to solve. We need to accept that no matter how bright each of the 
individuals are who develop these algorithms, their focus will necessarily be biased toward novelty related to outcomes 
rather than implementation. We are already seeing institutions trying to integrate multiple scanners with laboratory 
information systems, electronic medical records, and on-prem/cloud/hybrid data centers and standards like the OpenAPI 
are one of the tools that make this integration possible. 

So why is the [Association for Pathology Informatics](https://assoc-path-informatics.github.io/interop/) bringing 
attention to OpenAPI instead of say, HIMSS<sup> [2](https://www.himss.org/) </sup>? Well,
our theory is that it will be much easier to implement the innovative methods in AI/ML if we can develop more 
of an *easy lift* platform for our IT colleagues. Sorry Zuck, but the idea of "Move fast and break things" is not 
appropriate in the medical informatics domain. There's too much that could go wrong, too much liability and safety 
concerns, and too many people with diverse skill sets that have to be onboard to affect real change. Too often in 
academics it's easy to think about building an algorithm, publishing a paper, then moving on.  However, for an AI/ML 
algorithm to be implemented in the clinical space, we can't simply toss an academic-grade model "over-the-wall" to 
out IT colleagues, who may likely not understand the model, the framework, or even the programming language it was
written in.  It is not fair - or even realistic - to assume that these individuals could/should be responsible for 
making such an algorithm robust to various clinical factors that could negatively impact the results from real world 
data while at the same time asking them to make it available 24x7, robust from a security perspective, and build 
extensive middleware to adhere to custom requirements of the app and enforce institutional policies and standards. 


## Making the case for interoperability
The challenge is to present standards to developers whose goals may be more short-term oriented. We must make the 
case for why standards should be considered from the beginning to the end of the product life-cycle - while at the 
same time recognizing the constraints and minimizing the interoperability burden on any one group.  To do this, we need 
to agree first and foremost, that interoperability is needed. How many times have you wanted to "kick the tires" on 
some new AI model, only to realize that it would take a considerable amount of conversion effort so that it worked in 
your compute environment on your data? Sometimes, the amount of effort is daunting, and we aren't even sure that it will
be worth the effort in cases where the model performs worse than your existing strategy. 

Moreover, what happens when someone's model becomes deeply entrenched into a specific user interface or platform? If 
standards like open APIs are used at the outset, it becomes much simpler to disentangle the models from the 
interfaces.  Say for example, I want to compare a QC model that I developed in house to that of company X. My 
institution has decided to implement a platform from vendor Y. If company X's model is coupled to another platform 
whose APIs are closed, or not following standard practices, it may not be possible to consider company X's model since
it does not fit in to the enterprise context.  Even if the model is significantly better than anything else out there, 
that does not guarantee that it would be adopted because company Z's model is significantly better at something else.

## Using the OpenAPI spec in the context of digital pathology
In order to achieve interoperable software for digital pathology, it will be important for professional associations,
like API, to show how little additional effort standards adoption actually takes. Reading the details and getting down 
into the weeds can be overwhelming if there is not a clear picture of "What is it I actually need to know?". To this 
end, we are promoting highly-targeted primers like the one below that can help distill complex standards into 
bite-sized consumable pieces that are relevant to something we understand - digital pathology. We can always dig into 
the full specification to get the detailed answers to specific questions we may have.

So let's start with the basics. We will define our API in a YAML file. For this use case, let's say we want to create an
API that retrieves metadata about a slide.  From the [docs](https://spec.openapis.org/oas/v3.1.0#fixed-fields), we see
that there are 10 possible objects that we can add information to: openapi, info, jsonSchemaDialect, servers, paths,
webhooks, components, security, tags, and external docs.

### OpenAPI
The first object is pretty simple.  It's just an attestation of the OpenAPI specification you are conforming to. This 
means that as the specification evolves, our systems will be able to change their expectations of what the APIs should 
look like.  
```yaml
openapi: 3.1.0                              # The version of the OpenAPI spec your API is conforming to
```

### Info
The next object is where we can put some metadata about the API itself, including things like who can use it, license, and 
contact info.  Pretty basic stuff really. The `title` and `version` fields are the only required ones (as of v3.1.0).
```yaml
title: Metadata API
summary: Allows users to work with metadata for whole slide images
description: Retrieves and modified slide-level information from our internal servers 
termsOfService: https://example.com/terms/  # Where users can find the terms and conditions for this API use
contact:                                    # This little block provides info about who on your team is supporting this API
  name: API Support
  url: https://www.example.com/support
  email: support@example.com
license:                                    # License (if any)
  name: Apache 2.0
  url: https://www.apache.org/licenses/LICENSE-2.0.html
version: 1.0.1                              # Version of your API
```

### Server
An array of Server Objects, which provide connectivity information to a target server. In essence, this is where you
list the servers that you want your API to route to. You need these when your server needs to send the request to 
a different machine. Otherwise, the assumption is that you are only using the current machine (e.g. `/`).

```yaml
servers:
- url: https://dev.image-server.com/v1
  description: Development server
- url: https://stage.image-server.com/v1
  description: Staging server
- url: https://image-server.com/v1
  description: Production server
```

### Paths
OK, now that we have the plumbing out of the way, we can start to put in some business logic. We do this by 
1) Specifying the url paths (routes) we want to create
2) Defining the Inputs
3) Defining the outputs

Unlike the official docs, I'll provide a more realistic example for API-folks.  In this API, let's have the objective be
to query a slide (input) and get back the metadata about the slide (output).


Since I want the slideID to retreive metadata from a specific slide, I need to create a structure using a variable. For 
example, my URL will start with '/slideMetadata' and end with `{/slideID}`. If I didn't include the curly braces here, 
I would actually be creating a route that was '/slideMetadata/slideID' with the 'slideID' being literally 'slideID'.
```yaml
/slideMetadata/{slideID}:			# This is the route I want to create  
```
Now that I have the route defined, how do I tell the API what slide identifier to use as input? Simple, we just need
to create a [`requestBody`](https://spec.openapis.org/oas/v3.1.0#request-body-object) object.

```yaml
    parameters:
    - name: slideID 		# variable name must match the url variable
      in: path				# if you are using this parameter in the path,like we are, this must be set to 'path' 
	  						# More docs [here](https://spec.openapis.org/oas/v3.1.0#parameter-object)
      required: true		# This is required, since we need to know what slide to look for
      description: the slide identifier, as slideID 
      schema:
        type: string		# As in '10X12124ghsts.svs'
```
Great!  Now I have a route defined that takes a single variable.  The next step is to define what the API should return.
For this, we'll use a 'GET' request.
```yaml
  get:					# Since I am retrieving information, this is a GET-type request see [here](https://www.w3schools.com/tags/ref_httpmethods.asp)
    description: Returns all slide-level metadata	# Some human-readable information about what the API is doing
    responses:			
      '200':			# use [standard response codes](https://spec.openapis.org/oas/v3.1.0#httpCodes) wherever possible
        description: A list of all slide metadata keys and thier values.
        content:
          application/json:			# This specifies the response will be in JSON format
            schema:
              type: object			# Will return a dictionary object (otherwise integer, string, number)
              items:
                $ref: '#/components/schemas/OpenslideProperties'	# I'll explain this later
      '405': 			# If necessary, add other possible response codes
      	description: "Method Not Allowed",
      	content: 
        	application/json:
      				{...}	# Put content here corresponding to your response code
        }

```
In the above example, we created a single path (slideMetadata/{slideID}) with a single method (get), and two possible responses 
(200 and 405).  Naturally, the service that they are calling needs to have both of those options enabled/codified based
on your business logic. All of this makes sense, except for maybe that `$ref` thing, which is the next thing we will 
talk about (Schema Objects).

### Schema Objects
Schemas are simple standardised descriptions for the structure of the data that will be returned by the `slideMetadata` 
service. In this example, let's say that our `slideMetadata` service responds with 
[standard properties](https://openslide.org/api/python/#standard-properties). We need a way to represent that structure 
so that whatever code will eventually receive that response will know how to parse it. This is usually done by defining 
your schemas at the end of your `yaml` file like this:

```yaml
components:
  schemas:
    OpenslideProperties:	# From the example above, we said that the schema could be found in #/components/schemas/OpenslideProperties
      type: object			# Anything more complex that a string or int, should probably be an object or array
      properties:
		PROPERTY_NAME_COMMENT:
		  description: The name of the property containing a slide’s comment, if any
		  type: string
		PROPERTY_NAME_VENDOR:
		  description: The name of the property containing an identification of the vendor
		  type: string
		PROPERTY_NAME_QUICKHASH1:
		  description: The name of the property containing the “quickhash-1” sum
		  type: string
		PROPERTY_NAME_BACKGROUND_COLOR:
		  description: The name of the property containing a slide’s background color, if any. It is represented as an RGB hex triplet
		  type: string
		PROPERTY_NAME_OBJECTIVE_POWER:
		  description: The name of the property containing a slide’s objective power, if known
		  type: number
		PROPERTY_NAME_MPP_X:
		  description: The name of the property containing the number of microns per pixel in the X dimension of level 0, if known
		  type: float
		PROPERTY_NAME_MPP_Y:
		  description: The name of the property containing the number of microns per pixel in the Y dimension of level 0, if known
		  type: float
		PROPERTY_NAME_BOUNDS_X:
		  description: The name of the property containing the X coordinate of the rectangle bounding the non-empty region of the slide, if available
		  type: number
		PROPERTY_NAME_BOUNDS_Y:
		  description: The name of the property containing the Y coordinate of the rectangle bounding the non-empty region of the slide, if available
		  type: number
		PROPERTY_NAME_BOUNDS_WIDTH:
		  description: The name of the property containing the width of the rectangle bounding the non-empty region of the slide, if available
		  type: number
		PROPERTY_NAME_BOUNDS_HEIGHT:
		  description: The name of the property containing the height of the rectangle bounding the non-empty region of the slide, if available
		  type: number
```

There's a TON of documentation available for how to define the OpenAPI standard. I hope this brief intro with context
focused on digital pathology may have shown you how easy it would be to leverage these standards in your own workflows.
