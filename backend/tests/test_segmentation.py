from backend.scripts.rfm_segmentation import assign_segment

def test_champions_segment():
    segment = assign_segment(R=5, F=5, M=5)
    assert segment == "Champions"

def test_at_risk_segment():
    segment = assign_segment(R=1, F=2, M=2)
    assert segment == "At Risk"
