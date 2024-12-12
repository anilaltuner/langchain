from langchain import retrievers

EXPECTED_ALL = [
    "AmazonKendraRetriever",
    "AmazonKnowledgeBasesRetriever",
    "ArceeRetriever",
    "ArxivRetriever",
    "AzureAISearchRetriever",
    "AzureCognitiveSearchRetriever",
    "BM25Retriever",
    "ChaindeskRetriever",
    "ChatGPTPluginRetriever",
    "CohereRagRetriever",
    "ContextualCompressionRetriever",
    "DocArrayRetriever",
    "ElasticSearchBM25Retriever",
    "EmbedchainRetriever",
    "EnsembleRetriever",
    "GoogleCloudEnterpriseSearchRetriever",
    "GoogleDocumentAIWarehouseRetriever",
    "GoogleVertexAIMultiTurnSearchRetriever",
    "GoogleVertexAISearchRetriever",
    "KayAiRetriever",
    "KNNRetriever",
    "LlamaIndexGraphRetriever",
    "LlamaIndexRetriever",
    "MergerRetriever",
    "MetalRetriever",
    "MilvusRetriever",
    "MultiQueryRetriever",
    "MultiVectorRetriever",
    "NeuralDBRetriever",
    "OutlineRetriever",
    "ParentDocumentRetriever",
    "PineconeHybridSearchRetriever",
    "PubMedRetriever",
    "RemoteLangChainRetriever",
    "RePhraseQueryRetriever",
    "SelfQueryRetriever",
    "SVMRetriever",
    "TavilySearchAPIRetriever",
    "TFIDFRetriever",
    "TimeWeightedVectorStoreRetriever",
    "VespaRetriever",
    "WeaviateHybridSearchRetriever",
    "WebResearchRetriever",
    "WikipediaRetriever",
    "ZepRetriever",
    "ZillizRetriever",
]


def test_imports() -> None:
    assert sorted(retrievers.__all__) == sorted(EXPECTED_ALL)
