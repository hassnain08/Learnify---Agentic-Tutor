# Basic Integration Rules

This lesson covers fundamental integration rules.

## 1. Basic Integration Rules

* **Integrating Variables:** The integral of `dx` is `x + C`, where 'C' is the constant of integration. This applies to any variable (e.g., `∫dy = y + C`, `∫dt = t + C`).  The variable of integration must match the differential.

* **Integrating Constants:** The integral of a constant (k) multiplied by a variable is `kx + C`. For example, `∫5dx = 5x + C`.

* **Power Rule:**  The integral of `xⁿ dx` is `(xⁿ⁺¹)/(n+1) + C`. This rule does *not* apply when `n = -1`.

### Examples of the Power Rule:

* `∫x² dx = (x³/3) + C`
* `∫x³ dx = (x⁴/4) + C`
* `∫10x⁴ dx = 2x⁵ + C`
* `∫(1/x²) dx = ∫x⁻² dx = (-1/x) + C`  *(Rewrite before integrating!)*
* `∫(7/x⁴) dx = ∫7x⁻⁴ dx = (-7/(3x³)) + C`

* **Radical Functions:** Rewrite radical expressions as fractional exponents before applying the power rule.

    *Example:* `∫∛x dx = ∫x^(1/3) dx = (3/4)x^(4/3) + C`


## 2. Trigonometric Functions

Memorize these antiderivatives:

* `∫cos x dx = sin x + C`
* `∫sin x dx = -cos x + C`
* `∫sec²x dx = tan x + C`
* `∫sec x tan x dx = sec x + C`
* `∫csc²x dx = -cot x + C`
* `∫csc x cot x dx = -csc x + C`

### Examples:

* `∫(8cos x + 3sin x) dx = 8sin x - 3cos x + C`
* `∫(4sec²x - sec x tan x) dx = 4tan x - sec x + C`
* `∫(csc x cot x - csc²x) dx = -csc x + cot x + C` *(Rewrite before integrating!)*


## 3. Exponential Functions

* `∫eᵘ du = (eᵘ/u') + C` (where u' is the derivative of u, and u must be a linear function).

### Examples:

* `∫e⁴ˣ dx = (e⁴ˣ/4) + C`
* `∫e⁷ˣ⁻³ dx = (e⁷ˣ⁻³/7) + C`
* `∫eˣ dx = eˣ + C`

*Important Note:* `∫eˣ² dx` cannot be solved using this rule (the derivative of the exponent is not a constant).


## 4. Logarithmic Functions

* `∫(1/u) du = (ln|u|/u') + C` (where u' is the derivative of u, and u must be a linear function). The absolute value is crucial for handling negative arguments to ln.

### Examples:

* `∫(1/x) dx = ln|x| + C`
* `∫(1/(x+5)) dx = ln|x+5| + C`
* `∫(1/(4x-3)) dx = (1/4)ln|4x-3| + C`
* `∫(7/(3x-8)) dx = (7/3)ln|3x-8| + C`


## Checking Your Work

To verify your integration, differentiate your answer. You should obtain the original integrand.