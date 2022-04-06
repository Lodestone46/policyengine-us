from openfisca_us.model_api import *


class self_employment_social_security_tax(Variable):
    value_type = float
    entity = Person
    label = "Self-employment Social Security tax"
    definition_period = YEAR
    unit = USD

    def formula(person, period, parameters):
        rate = parameters(period).irs.self_employment.social_security_rate
        return rate * person("payroll_taxable_self_employment_income", period)
