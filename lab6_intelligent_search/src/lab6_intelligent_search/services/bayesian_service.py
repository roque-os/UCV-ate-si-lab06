from lab6_intelligent_search.bayesian.disease_network import inference

def query_disease(fever: int, test: int):
    result = inference.query(
        variables=['Disease'],
        evidence={'Fever': fever, 'Test': test}
    )
    return {'result': str(result)}