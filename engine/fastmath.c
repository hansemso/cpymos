#include <stdio.h>
#include <ctype.h>
#include <math.h>

const char *expr_ptr;

double parse_expression();  // forward

double parse_number() {
    double result = 0.0;
    while (isspace(*expr_ptr)) expr_ptr++;

    if (*expr_ptr == '(') {
        expr_ptr++; // skip '('
        result = parse_expression();
        if (*expr_ptr == ')') expr_ptr++; // skip ')'
        return result;
    }

    while (isdigit(*expr_ptr) || *expr_ptr == '.') {
        if (*expr_ptr == '.') {
            expr_ptr++;
            double frac = 0.1;
            while (isdigit(*expr_ptr)) {
                result += (*expr_ptr - '0') * frac;
                frac /= 10;
                expr_ptr++;
            }
            return result;
        } else {
            result = result * 10 + (*expr_ptr - '0');
            expr_ptr++;
        }
    }

    return result;
}

double parse_factor() {
    double result = parse_number();
    while (*expr_ptr == '^') {
        expr_ptr++;
        double rhs = parse_factor();  // right-associative
        result = pow(result, rhs);
    }
    return result;
}

double parse_term() {
    double result = parse_factor();
    while (*expr_ptr == '*' || *expr_ptr == '/') {
        char op = *expr_ptr;
        expr_ptr++;
        double rhs = parse_factor();
        if (op == '*') result *= rhs;
        else result /= rhs;
    }
    return result;
}

double parse_expression() {
    double result = parse_term();
    while (*expr_ptr == '+' || *expr_ptr == '-') {
        char op = *expr_ptr;
        expr_ptr++;
        double rhs = parse_term();
        if (op == '+') result += rhs;
        else result -= rhs;
    }
    return result;
}

// Expose for Python
__declspec(dllexport) double eval_numeric(const char *expr) {
    expr_ptr = expr;
    return parse_expression();
}

// Optional: standalone fast_pow
__declspec(dllexport) double fast_pow(double base, double exp) {
    return pow(base, exp);
}