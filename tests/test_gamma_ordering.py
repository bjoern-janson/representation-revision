from representation_revision.gamma_ordering import q_values_for_leaf_triple


def test_q_values_are_reversal_paired():
    labels = ("a", "b", "d")
    distance = {
        ("a", "b"): 2, ("b", "a"): 2,
        ("a", "d"): 5, ("d", "a"): 5,
        ("b", "d"): 7, ("d", "b"): 7,
    }
    rows = q_values_for_leaf_triple(labels, lambda x, y: distance[(x, y)])
    assert len(rows) == 6
    by_order = {tuple(row["order"]): row["q"] for row in rows}
    assert by_order[("a", "b", "d")] == by_order[("d", "b", "a")]
    assert len(set(by_order.values())) == 3


def test_equilateral_toy_is_order_invariant():
    rows = q_values_for_leaf_triple(("a", "b", "d"), lambda _x, _y: 4)
    assert {row["q"] for row in rows} == {8}


def test_dry_validation_reports_frozen_fixture_shape():
    from representation_revision.gamma_ordering import run_gamma_ordering

    result = run_gamma_ordering(dry_validate_only=True)
    assert result["syntax_members"] == 77
    assert result["semantic_classes"] == 6
    assert result["eligible_motifs"] == 116664
    assert result["semantic_pairs"] == 759


def test_profile_l1_matrix_is_symmetric_with_zero_diagonal():
    from representation_revision.gamma_ordering import profile_l1_matrix

    profiles = ((0, 2, 4), (1, 2, 1), (3, 0, 4))
    matrix = profile_l1_matrix(profiles)
    assert matrix == (
        (0, 4, 5),
        (4, 0, 7),
        (5, 7, 0),
    )


def test_summarize_q_rows_counts_distinct_values_and_range():
    from representation_revision.gamma_ordering import summarize_q_rows

    summary = summarize_q_rows([
        {"order": ["a", "b", "d"], "q": 9},
        {"order": ["d", "b", "a"], "q": 9},
        {"order": ["a", "d", "b"], "q": 12},
        {"order": ["b", "d", "a"], "q": 12},
        {"order": ["b", "a", "d"], "q": 7},
        {"order": ["d", "a", "b"], "q": 7},
    ])
    assert summary == {"distinct_q_count": 3, "delta_q": 5}


def test_analyze_motifs_requires_same_motif_positive_in_all_families():
    from representation_revision.gamma_ordering import analyze_motifs

    syntax = ("a", "b", "c", "d")
    classes = ({"members": list(syntax)},)
    non_equilateral = (
        (0, 1, 2, 3),
        (1, 0, 4, 5),
        (2, 4, 0, 6),
        (3, 5, 6, 0),
    )
    equilateral = (
        (0, 1, 1, 1),
        (1, 0, 1, 1),
        (1, 1, 0, 1),
        (1, 1, 1, 0),
    )
    blocked = analyze_motifs(
        syntax,
        classes,
        {"R_v1": non_equilateral, "R_unit": non_equilateral, "R_depth": equilateral},
        expected_eligible=None,
    )
    assert blocked["eligible_motifs"] == 4
    assert blocked["common_positive_motifs"] == 0
    assert blocked["primary_positive"] is False

    common = analyze_motifs(
        syntax,
        classes,
        {"R_v1": non_equilateral, "R_unit": non_equilateral, "R_depth": non_equilateral},
        expected_eligible=None,
    )
    assert common["common_positive_motifs"] == 4
    assert common["primary_positive"] is True
    assert common["witness"]["center"] == "a"
    assert common["witness"]["leaves"] == ["b", "c", "d"]


def test_predecessor_profile_separation_counts_match_frozen_v2():
    from boolean_world.ast import parse_canonical
    from representation_revision.accessibility import resistance
    from representation_revision.resistance_robustness import unit_resistance, depth_resistance
    from representation_revision.gamma_ordering import load_fixtures, build_profiles

    syntax, semantic = load_fixtures()
    nodes = tuple(parse_canonical(text) for text in syntax)
    families = {
        "R_v1": resistance,
        "R_unit": unit_resistance,
        "R_depth": depth_resistance,
    }
    profiles = {name: build_profiles(nodes, fn) for name, fn in families.items()}
    index = {text: i for i, text in enumerate(syntax)}
    pairs = []
    for record in semantic["classes"]:
        members = [index[text] for text in record["members"]]
        for pos, i in enumerate(members):
            for j in members[pos + 1:]:
                pairs.append((i, j))
    assert len(pairs) == 759
    for name in families:
        assert sum(profiles[name][i] != profiles[name][j] for i, j in pairs) == 759


def test_component_runner_composes_profiles_distances_and_motif_analysis_on_toy_universe():
    from representation_revision.gamma_ordering import run_gamma_ordering_from_components

    syntax = ("a", "b", "c", "d")
    semantic = {"classes": [{"members": list(syntax)}]}
    nodes = (0, 1, 2, 3)
    families = {
        "R_v1": lambda x, y: abs(x - y),
        "R_unit": lambda x, y: abs(x - y),
        "R_depth": lambda x, y: abs(x - y),
    }
    result = run_gamma_ordering_from_components(
        syntax,
        semantic,
        nodes,
        families,
        expected_eligible=4,
    )
    assert result["eligible_motifs"] == 4
    assert result["primary_positive"] is True
    assert set(result["families"]) == {"R_v1", "R_unit", "R_depth"}


def test_canonical_json_is_repeatable():
    from run_gamma_ordering import canonical_json

    assert canonical_json({"b": 2, "a": 1}) == '{"a":1,"b":2}\n'
