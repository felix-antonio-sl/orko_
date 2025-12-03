#!/usr/bin/env python3
"""
impl_cap22_run.py — CAP-22 validation runner

Usa valores simulados (extraídos de artefactos.md) para reproducir H_org y E6_current.
Valida la implementación de las fórmulas de las calculadoras.
"""
import math


def compute_H_org(A, B, C, D, E):
    """
    Calcula H_org a partir de los 5 componentes H_A..H_E.
    
    Formula: H_org = 0.30*H_A + 0.25*H_B + 0.20*H_C + 0.15*H_D + 0.10*H_E
    
    Args:
        A, B, C, D, E: Componentes H_A, H_B, H_C, H_D, H_E (0-100)
    
    Returns:
        H_org (0-100)
    """
    return 0.30 * A + 0.25 * B + 0.20 * C + 0.15 * D + 0.10 * E


def compute_E6(H_org, tf1, tf2, tf3, complexity):
    """
    Calcula E6_current a partir de H_org, TF scores y complejidad contextual.
    
    Formula:
        Base = 0.60 * (H_org/100) + 0.40 * (tf1+tf2+tf3)/3
        CF = clamp((complexity - 1)/5, 0, 0.40)
        E6_current = Base * (1 - CF)
    
    Args:
        H_org: Health score organizacional (0-100)
        tf1, tf2, tf3: Tissue fabric scores (0-1)
        complexity: Context complexity level (1-6)
    
    Returns:
        E6_current (0-1)
    """
    Hn = H_org / 100.0
    tf_avg = (tf1 + tf2 + tf3) / 3.0
    base = 0.60 * Hn + 0.40 * tf_avg
    
    # Complexity factor: penaliza entre 0% y 40% según complejidad
    cf = max(0.0, min((complexity - 1.0) / 5.0, 0.40))
    
    return round(base * (1 - cf), 3)


def demo_startup():
    """
    Caso 01: startup 50 personas
    Valores extraídos de artefactos.md
    """
    # Componentes H_org
    A = 68.0  # Strategic Alignment
    B = 70.0  # Capacity
    C = 78.0  # Flow
    D = 78.0  # Information
    E = 70.0  # Decision
    
    # Tissue fabric scores
    tf1 = 0.70
    tf2 = 0.68
    tf3 = 0.78
    
    H = compute_H_org(A, B, C, D, E)
    E6 = compute_E6(H, tf1, tf2, tf3, complexity=3)
    
    return {"H_org": round(H, 2), "E6_current": E6}


def demo_gore_nuble():
    """
    Caso 06: GORE Ñuble (gobierno regional)
    Valores extraídos de artefactos.md
    """
    # Componentes H_org
    A = 62.0  # Strategic Alignment
    B = 72.0  # Capacity
    C = 62.0  # Flow
    D = 62.0  # Information
    E = 64.0  # Decision
    
    # Tissue fabric scores
    tf1 = 0.65
    tf2 = 0.62
    tf3 = 0.62
    
    H = compute_H_org(A, B, C, D, E)
    E6 = compute_E6(H, tf1, tf2, tf3, complexity=4)
    
    return {"H_org": round(H, 2), "E6_current": E6}


def validate_results():
    """
    Valida que los resultados coincidan con los valores esperados.
    """
    print("=" * 60)
    print("CAP-22 Validation - Health Score & E6 Calculator")
    print("=" * 60)
    
    # Caso 01
    result_01 = demo_startup()
    print("\nCASO 01 (startup 50p):", result_01)
    print("  Esperado: H_org ≈ 72, E6_current ≈ 0.43")
    
    # Validación
    h_org_ok = abs(result_01["H_org"] - 72.0) <= 2.0
    e6_ok = abs(result_01["E6_current"] - 0.43) <= 0.02
    
    print(f"  ✓ H_org: {'PASS' if h_org_ok else 'FAIL'}")
    print(f"  ✓ E6_current: {'PASS' if e6_ok else 'FAIL'}")
    
    # Caso 06
    result_06 = demo_gore_nuble()
    print("\nCASO 06 (GORE Ñuble):", result_06)
    print("  Esperado: H_org ≈ 66, E6_current ≈ 0.38")
    
    # Validación
    h_org_ok_06 = abs(result_06["H_org"] - 66.0) <= 2.0
    e6_ok_06 = abs(result_06["E6_current"] - 0.38) <= 0.02
    
    print(f"  ✓ H_org: {'PASS' if h_org_ok_06 else 'FAIL'}")
    print(f"  ✓ E6_current: {'PASS' if e6_ok_06 else 'FAIL'}")
    
    # Resultado final
    all_pass = h_org_ok and e6_ok and h_org_ok_06 and e6_ok_06
    
    print("\n" + "=" * 60)
    if all_pass:
        print("✓ VALIDACIÓN COMPLETA: TODOS LOS TESTS PASARON")
    else:
        print("✗ VALIDACIÓN FALLÓ: REVISAR FÓRMULAS")
    print("=" * 60)
    
    return all_pass


if __name__ == "__main__":
    success = validate_results()
    exit(0 if success else 1)
