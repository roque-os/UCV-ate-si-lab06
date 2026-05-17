from lab6_intelligent_search.bayesian.disease_network import inference

def test_bayesian():
    result = inference.query(
        variables=['Disease'],
        evidence={'Fever': 1, 'Test': 1}
    )
    assert result is not None