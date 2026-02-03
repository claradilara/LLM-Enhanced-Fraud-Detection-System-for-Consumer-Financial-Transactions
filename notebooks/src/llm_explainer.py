"""
LLM Fraud Explanation Module

This module converts fraud model outputs and engineered features
into human-readable explanations for fraud analysts.
"""

from typing import Dict


class FraudLLMExplainer:
    def __init__(self, llm_client=None):
        """
        Parameters
        ----------
        llm_client : object
            Optional LLM client (OpenAI, local LLM, etc.)
            If None, explanations are rule-based (fallback mode).
        """
        self.llm_client = llm_client

    def build_prompt(self, features: Dict, fraud_score: float) -> str:
        """
        Build a structured prompt for the LLM.
        """
        prompt = f"""
You are a fraud risk analyst at a financial institution.

A transaction has been flagged by a fraud detection model.

Fraud probability: {fraud_score:.2f}

Transaction risk indicators:
- Abnormal amount (z-score): {features.get("amt_zscore")}
- Transactions today (card): {features.get("card_txn_count_day")}
- Total amount today: {features.get("card_amt_sum_day")}
- Time since previous transaction (seconds): {features.get("time_since_prev_txn")}
- Missing identity signals: {features.get("missing_identity_count")}
- High amount flag: {features.get("high_amount_flag")}
- Night transaction flag: {features.get("night_transaction_flag")}

Explain in clear, non-technical language why this transaction may be fraudulent.
Focus on behavioral patterns rather than technical model details.
"""
        return prompt.strip()

    def explain_with_llm(self, prompt: str) -> str:
        """
        Call the LLM API (placeholder).
        """
        # Example interface — replace with real LLM call
        response = self.llm_client.generate(prompt)
        return response

    def explain_rule_based(self, features: Dict, fraud_score: float) -> str:
        """
        Fallback explanation without LLM (important for robustness).
        """
        reasons = []

        if features.get("amt_zscore", 0) > 3:
            reasons.append("the transaction amount is unusually high compared to past behavior")

        if features.get("card_txn_count_day", 0) > 5:
            reasons.append("there is an unusually high number of transactions in a short time")

        if features.get("time_since_prev_txn", 0) >= 0 and features.get("time_since_prev_txn") < 60:
            reasons.append("transactions are occurring in rapid succession")

        if features.get("missing_identity_count", 0) > 5:reasons.append(
        "important device or identity information is missing, which limits the ability to verify the customer")

        if features.get("night_transaction_flag") == 1:
            reasons.append("the transaction occurred during an unusual time of day")

        if not reasons:
            reasons.append("the transaction shows multiple subtle risk signals")

        explanation = (
            f"This transaction was flagged with a fraud probability of {fraud_score:.2f} because "
            + ", ".join(reasons)
            + "."
        )

        return explanation

    def explain(self, features: Dict, fraud_score: float) -> str:
        """
        Main entry point.
        """
        prompt = self.build_prompt(features, fraud_score)

        if self.llm_client:
            return self.explain_with_llm(prompt)

        return self.explain_rule_based(features, fraud_score)
