def get_learning_roadmap(target_role, missing_skills, roles):
    """Return a role-specific roadmap, prioritizing skill gaps."""
    roadmap = roles[target_role]["roadmap"]
    if missing_skills:
        first = "Prioritize these skill gaps: " + ", ".join(missing_skills[:4])
        return [first] + roadmap
    return ["Maintain your skills with regular practice."] + roadmap
