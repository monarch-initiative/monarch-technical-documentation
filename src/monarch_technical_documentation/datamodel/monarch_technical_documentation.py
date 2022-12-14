# Auto generated from monarch_technical_documentation.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-12-04T12:28:37
# Schema: monarch-documentation-schema
#
# id: https://w3id.org/monarch-initiative/monarch-technical-documentation
# description: Technical documentation for all Monarch applications, packages, services and related projects.
# license: GNU GPL v3.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MTD = CurieNamespace('mtd', 'https://w3id.org/monarch-initiative/monarch-technical-documentation/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = MTD


# Types

# Class references
class ResourceId(URIorCURIE):
    pass


class DataAssetId(ResourceId):
    pass


class StandardId(ResourceId):
    pass


class ToolId(ResourceId):
    pass


class DocumentationId(ResourceId):
    pass


class RepositoryId(ResourceId):
    pass


class ResourceRegistryId(ResourceId):
    pass


@dataclass
class Resource(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = MTD.Resource

    id: Union[str, ResourceId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    grants: Optional[Union[Union[str, "GrantEnum"], List[Union[str, "GrantEnum"]]]] = empty_list()
    documentation: Optional[Union[str, URIorCURIE]] = None
    monarch_contribution: Optional[Union[str, "MonarchContributionEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourceId):
            self.id = ResourceId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.grants, list):
            self.grants = [self.grants] if self.grants is not None else []
        self.grants = [v if isinstance(v, GrantEnum) else GrantEnum(v) for v in self.grants]

        if self.documentation is not None and not isinstance(self.documentation, URIorCURIE):
            self.documentation = URIorCURIE(self.documentation)

        if self.monarch_contribution is not None and not isinstance(self.monarch_contribution, MonarchContributionEnum):
            self.monarch_contribution = MonarchContributionEnum(self.monarch_contribution)

        super().__post_init__(**kwargs)


@dataclass
class DataAsset(Resource):
    """
    A data asset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.DataAsset
    class_class_curie: ClassVar[str] = "mtd:DataAsset"
    class_name: ClassVar[str] = "DataAsset"
    class_model_uri: ClassVar[URIRef] = MTD.DataAsset

    id: Union[str, DataAssetId] = None
    download: Optional[Union[dict, "Download"]] = None
    category: Optional[Union[str, "DataAssetEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataAssetId):
            self.id = DataAssetId(self.id)

        if self.download is not None and not isinstance(self.download, Download):
            self.download = Download(**as_dict(self.download))

        if self.category is not None and not isinstance(self.category, DataAssetEnum):
            self.category = DataAssetEnum(self.category)

        super().__post_init__(**kwargs)


@dataclass
class Standard(Resource):
    """
    A reference to a repository.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.Standard
    class_class_curie: ClassVar[str] = "mtd:Standard"
    class_name: ClassVar[str] = "Standard"
    class_model_uri: ClassVar[URIRef] = MTD.Standard

    id: Union[str, StandardId] = None
    category: Optional[Union[str, "StandardEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StandardId):
            self.id = StandardId(self.id)

        if self.category is not None and not isinstance(self.category, StandardEnum):
            self.category = StandardEnum(self.category)

        super().__post_init__(**kwargs)


@dataclass
class Tool(Resource):
    """
    A reference to a repository.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.Tool
    class_class_curie: ClassVar[str] = "mtd:Tool"
    class_name: ClassVar[str] = "Tool"
    class_model_uri: ClassVar[URIRef] = MTD.Tool

    id: Union[str, ToolId] = None
    url: Optional[Union[str, URIorCURIE]] = None
    repository: Optional[Union[str, URIorCURIE]] = None
    category: Optional[Union[str, "ToolAssetEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ToolId):
            self.id = ToolId(self.id)

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        if self.repository is not None and not isinstance(self.repository, URIorCURIE):
            self.repository = URIorCURIE(self.repository)

        if self.category is not None and not isinstance(self.category, ToolAssetEnum):
            self.category = ToolAssetEnum(self.category)

        super().__post_init__(**kwargs)


@dataclass
class Documentation(Resource):
    """
    A reference to a documentation page.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.Documentation
    class_class_curie: ClassVar[str] = "mtd:Documentation"
    class_name: ClassVar[str] = "Documentation"
    class_model_uri: ClassVar[URIRef] = MTD.Documentation

    id: Union[str, DocumentationId] = None
    url: Optional[Union[str, URIorCURIE]] = None
    repository: Optional[Union[str, URIorCURIE]] = None
    category: Optional[Union[str, "DocumentationAssetEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DocumentationId):
            self.id = DocumentationId(self.id)

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        if self.repository is not None and not isinstance(self.repository, URIorCURIE):
            self.repository = URIorCURIE(self.repository)

        if self.category is not None and not isinstance(self.category, DocumentationAssetEnum):
            self.category = DocumentationAssetEnum(self.category)

        super().__post_init__(**kwargs)


@dataclass
class Repository(Resource):
    """
    A reference to a version control repository.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.Repository
    class_class_curie: ClassVar[str] = "mtd:Repository"
    class_name: ClassVar[str] = "Repository"
    class_model_uri: ClassVar[URIRef] = MTD.Repository

    id: Union[str, RepositoryId] = None
    depends_on: Optional[Union[str, RepositoryId]] = None
    repo_url: Optional[str] = None
    organization: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RepositoryId):
            self.id = RepositoryId(self.id)

        if self.depends_on is not None and not isinstance(self.depends_on, RepositoryId):
            self.depends_on = RepositoryId(self.depends_on)

        if self.repo_url is not None and not isinstance(self.repo_url, str):
            self.repo_url = str(self.repo_url)

        if self.organization is not None and not isinstance(self.organization, str):
            self.organization = str(self.organization)

        super().__post_init__(**kwargs)


@dataclass
class ResourceRegistry(Resource):
    """
    A registry of different types of data assets
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.ResourceRegistry
    class_class_curie: ClassVar[str] = "mtd:ResourceRegistry"
    class_name: ClassVar[str] = "ResourceRegistry"
    class_model_uri: ClassVar[URIRef] = MTD.ResourceRegistry

    id: Union[str, ResourceRegistryId] = None
    data: Optional[Union[Dict[Union[str, DataAssetId], Union[dict, DataAsset]], List[Union[dict, DataAsset]]]] = empty_dict()
    standards: Optional[Union[Dict[Union[str, StandardId], Union[dict, Standard]], List[Union[dict, Standard]]]] = empty_dict()
    tools: Optional[Union[Dict[Union[str, ToolId], Union[dict, Tool]], List[Union[dict, Tool]]]] = empty_dict()
    documentations: Optional[Union[Dict[Union[str, DocumentationId], Union[dict, Documentation]], List[Union[dict, Documentation]]]] = empty_dict()
    repositories: Optional[Union[Dict[Union[str, ResourceId], Union[dict, Resource]], List[Union[dict, Resource]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourceRegistryId):
            self.id = ResourceRegistryId(self.id)

        self._normalize_inlined_as_list(slot_name="data", slot_type=DataAsset, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="standards", slot_type=Standard, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="tools", slot_type=Tool, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="documentations", slot_type=Documentation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="repositories", slot_type=Resource, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Download(YAMLRoot):
    """
    A downloadable asset, i.e. a data file, an software component, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MTD.Download
    class_class_curie: ClassVar[str] = "mtd:Download"
    class_name: ClassVar[str] = "Download"
    class_model_uri: ClassVar[URIRef] = MTD.Download

    url: Optional[str] = None
    release_status: Optional[str] = None
    file_format: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.release_status is not None and not isinstance(self.release_status, str):
            self.release_status = str(self.release_status)

        if self.file_format is not None and not isinstance(self.file_format, str):
            self.file_format = str(self.file_format)

        super().__post_init__(**kwargs)


# Enumerations
class ReleaseStatusEnum(EnumDefinitionImpl):

    public = PermissibleValue(text="public")

    _defn = EnumDefinition(
        name="ReleaseStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "development snapshot",
                PermissibleValue(text="development snapshot") )

class FileFormatEnum(EnumDefinitionImpl):

    tsv = PermissibleValue(text="tsv")
    csv = PermissibleValue(text="csv")
    ttl = PermissibleValue(text="ttl")
    json = PermissibleValue(text="json")
    rdfxml = PermissibleValue(text="rdfxml")

    _defn = EnumDefinition(
        name="FileFormatEnum",
    )

class StandardEnum(EnumDefinitionImpl):

    Ontology = PermissibleValue(text="Ontology")

    _defn = EnumDefinition(
        name="StandardEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Data Standard",
                PermissibleValue(text="Data Standard") )
        setattr(cls, "Data Exchange",
                PermissibleValue(text="Data Exchange") )

class DataAssetEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DataAssetEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Biomedical Data",
                PermissibleValue(text="Biomedical Data") )
        setattr(cls, "Knowledge Graph Ingestibles",
                PermissibleValue(text="Knowledge Graph Ingestibles") )
        setattr(cls, "Knowledge Graph",
                PermissibleValue(text="Knowledge Graph") )

class ToolAssetEnum(EnumDefinitionImpl):

    Mapping = PermissibleValue(text="Mapping")

    _defn = EnumDefinition(
        name="ToolAssetEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Clinical Diagnosis",
                PermissibleValue(text="Clinical Diagnosis") )
        setattr(cls, "Ontology Maintenance",
                PermissibleValue(text="Ontology Maintenance") )
        setattr(cls, "Ontology Use",
                PermissibleValue(text="Ontology Use") )
        setattr(cls, "Data Curation",
                PermissibleValue(text="Data Curation") )

class DocumentationAssetEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DocumentationAssetEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Technical Documentation",
                PermissibleValue(text="Technical Documentation") )

class MonarchContributionEnum(EnumDefinitionImpl):

    Lead = PermissibleValue(text="Lead")
    Contributor = PermissibleValue(text="Contributor")

    _defn = EnumDefinition(
        name="MonarchContributionEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Co-Lead",
                PermissibleValue(text="Co-Lead") )

class GrantEnum(EnumDefinitionImpl):

    HPO = PermissibleValue(text="HPO")
    Exomiser = PermissibleValue(text="Exomiser")

    _defn = EnumDefinition(
        name="GrantEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Phenomics First",
                PermissibleValue(text="Phenomics First",
                                 description="The Phenomics First Grant") )
        setattr(cls, "Monarch R24",
                PermissibleValue(text="Monarch R24") )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MTD.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MTD.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MTD.description, domain=None, range=Optional[str])

slots.download = Slot(uri=MTD.download, name="download", curie=MTD.curie('download'),
                   model_uri=MTD.download, domain=None, range=Optional[Union[dict, Download]])

slots.grants = Slot(uri=MTD.grants, name="grants", curie=MTD.curie('grants'),
                   model_uri=MTD.grants, domain=None, range=Optional[Union[Union[str, "GrantEnum"], List[Union[str, "GrantEnum"]]]])

slots.release_status = Slot(uri=MTD.release_status, name="release_status", curie=MTD.curie('release_status'),
                   model_uri=MTD.release_status, domain=None, range=Optional[Union[str, "ReleaseStatusEnum"]])

slots.repository = Slot(uri=MTD.repository, name="repository", curie=MTD.curie('repository'),
                   model_uri=MTD.repository, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.file_format = Slot(uri=MTD.file_format, name="file_format", curie=MTD.curie('file_format'),
                   model_uri=MTD.file_format, domain=None, range=Optional[Union[str, "FileFormatEnum"]])

slots.url = Slot(uri=MTD.url, name="url", curie=MTD.curie('url'),
                   model_uri=MTD.url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.category = Slot(uri=MTD.category, name="category", curie=MTD.curie('category'),
                   model_uri=MTD.category, domain=None, range=Optional[str])

slots.documentation = Slot(uri=MTD.documentation, name="documentation", curie=MTD.curie('documentation'),
                   model_uri=MTD.documentation, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.monarch_contribution = Slot(uri=MTD.monarch_contribution, name="monarch_contribution", curie=MTD.curie('monarch_contribution'),
                   model_uri=MTD.monarch_contribution, domain=None, range=Optional[Union[str, "MonarchContributionEnum"]])

slots.data = Slot(uri=MTD.data, name="data", curie=MTD.curie('data'),
                   model_uri=MTD.data, domain=None, range=Optional[Union[Dict[Union[str, DataAssetId], Union[dict, DataAsset]], List[Union[dict, DataAsset]]]])

slots.standards = Slot(uri=MTD.standards, name="standards", curie=MTD.curie('standards'),
                   model_uri=MTD.standards, domain=None, range=Optional[Union[Dict[Union[str, StandardId], Union[dict, Standard]], List[Union[dict, Standard]]]])

slots.tools = Slot(uri=MTD.tools, name="tools", curie=MTD.curie('tools'),
                   model_uri=MTD.tools, domain=None, range=Optional[Union[Dict[Union[str, ToolId], Union[dict, Tool]], List[Union[dict, Tool]]]])

slots.documentations = Slot(uri=MTD.documentations, name="documentations", curie=MTD.curie('documentations'),
                   model_uri=MTD.documentations, domain=None, range=Optional[Union[Dict[Union[str, DocumentationId], Union[dict, Documentation]], List[Union[dict, Documentation]]]])

slots.repositories = Slot(uri=MTD.repositories, name="repositories", curie=MTD.curie('repositories'),
                   model_uri=MTD.repositories, domain=None, range=Optional[Union[Dict[Union[str, ResourceId], Union[dict, Resource]], List[Union[dict, Resource]]]])

slots.depends_on = Slot(uri=MTD.depends_on, name="depends_on", curie=MTD.curie('depends_on'),
                   model_uri=MTD.depends_on, domain=Repository, range=Optional[Union[str, RepositoryId]])

slots.repo_url = Slot(uri=MTD.repo_url, name="repo_url", curie=MTD.curie('repo_url'),
                   model_uri=MTD.repo_url, domain=None, range=Optional[str])

slots.organization = Slot(uri=MTD.organization, name="organization", curie=MTD.curie('organization'),
                   model_uri=MTD.organization, domain=None, range=Optional[str])

slots.download__url = Slot(uri=MTD.url, name="download__url", curie=MTD.curie('url'),
                   model_uri=MTD.download__url, domain=None, range=Optional[str])

slots.download__release_status = Slot(uri=MTD.release_status, name="download__release_status", curie=MTD.curie('release_status'),
                   model_uri=MTD.download__release_status, domain=None, range=Optional[str])

slots.download__file_format = Slot(uri=MTD.file_format, name="download__file_format", curie=MTD.curie('file_format'),
                   model_uri=MTD.download__file_format, domain=None, range=Optional[str])

slots.DataAsset_category = Slot(uri=MTD.category, name="DataAsset_category", curie=MTD.curie('category'),
                   model_uri=MTD.DataAsset_category, domain=DataAsset, range=Optional[Union[str, "DataAssetEnum"]])

slots.Standard_category = Slot(uri=MTD.category, name="Standard_category", curie=MTD.curie('category'),
                   model_uri=MTD.Standard_category, domain=Standard, range=Optional[Union[str, "StandardEnum"]])

slots.Tool_category = Slot(uri=MTD.category, name="Tool_category", curie=MTD.curie('category'),
                   model_uri=MTD.Tool_category, domain=Tool, range=Optional[Union[str, "ToolAssetEnum"]])

slots.Documentation_category = Slot(uri=MTD.category, name="Documentation_category", curie=MTD.curie('category'),
                   model_uri=MTD.Documentation_category, domain=Documentation, range=Optional[Union[str, "DocumentationAssetEnum"]])
