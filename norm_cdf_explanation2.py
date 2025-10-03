import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.integrate import quad

# Let's demonstrate how norm.cdf() computes percentiles

def demonstrate_cdf_calculation():
    """
    Demonstrate how norm.cdf() calculates percentiles using the standard normal distribution
    """
    print("=== Understanding norm.cdf() and Percentiles ===\n")
    
    # The standard normal distribution has mean=0, std=1
    print("Standard Normal Distribution: μ = 0, σ = 1")
    print("The probability density function (PDF) is:")
    print("f(x) = (1/√(2π)) * e^(-x²/2)")
    print()
    
    # Show some example calculations
    z_values = [-3, -2, -1, 0, 1, 2, 3]
    
    print("Z-Score | CDF Value | Percentile | Meaning")
    print("-" * 55)
    
    for z in z_values:
        cdf_value = norm.cdf(z)
        percentile = cdf_value * 100
        print(f"{z:7.1f} | {cdf_value:9.6f} | {percentile:9.2f}% | {get_meaning(z, percentile)}")
    
    print()
    print("=== What CDF Actually Computes ===")
    print("CDF(z) = P(Z ≤ z) = ∫_{-∞}^{z} f(x) dx")
    print("This is the area under the curve from -∞ to z")
    print()

def get_meaning(z, percentile):
    """Get human-readable meaning of the percentile"""
    if z == 0:
        return "Exactly at the mean"
    elif z < 0:
        return f"{percentile:.1f}% of values are below this point"
    else:
        return f"{percentile:.1f}% of values are below this point"

def manual_cdf_approximation(z, n_intervals=1000):
    """
    Manually approximate the CDF using numerical integration
    This shows what norm.cdf() is essentially doing behind the scenes
    """
    
    def standard_normal_pdf(x):
        """Standard normal probability density function"""
        return (1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)
    
    # Integrate from a very negative number to z
    # (we use -10 instead of -∞ because the probability beyond -10 is negligible)
    lower_bound = -10
    
    # Use numerical integration (trapezoidal rule)
    x_values = np.linspace(lower_bound, z, n_intervals)
    y_values = [standard_normal_pdf(x) for x in x_values]
    
    # Trapezoidal rule approximation
    dx = (z - lower_bound) / (n_intervals - 1)
    integral = dx * (y_values[0]/2 + sum(y_values[1:-1]) + y_values[-1]/2)
    
    return integral

def compare_methods():
    """Compare scipy's norm.cdf() with our manual approximation"""
    print("\n=== Comparing Methods ===")
    print("Z-Score | scipy.norm.cdf | Manual Integration | Difference")
    print("-" * 65)
    
    test_z_values = [-2.0, -1.0, 0.0, 1.0, 2.0]
    
    for z in test_z_values:
        scipy_result = norm.cdf(z)
        manual_result = manual_cdf_approximation(z)
        difference = abs(scipy_result - manual_result)
        
        print(f"{z:7.1f} | {scipy_result:14.8f} | {manual_result:18.8f} | {difference:.2e}")

def visualize_cdf_concept():
    """Create a visualization showing how CDF relates to the area under the curve"""
    
    # Generate x values for the normal distribution
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x)  # Probability density function
    
    # Create the plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Left plot: Show PDF with shaded area for z = -1
    z_example = -1.0
    x_fill = x[x <= z_example]
    y_fill = norm.pdf(x_fill)
    
    ax1.plot(x, y, 'b-', linewidth=2, label='Standard Normal PDF')
    ax1.fill_between(x_fill, y_fill, alpha=0.3, color='red', 
                     label=f'Area = CDF({z_example}) = {norm.cdf(z_example):.4f}')
    ax1.axvline(z_example, color='red', linestyle='--', linewidth=2)
    ax1.set_xlabel('Z-Score')
    ax1.set_ylabel('Probability Density')
    ax1.set_title(f'PDF: Shaded area = {norm.cdf(z_example)*100:.2f} percentile')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Right plot: Show the CDF function
    x_cdf = np.linspace(-4, 4, 1000)
    y_cdf = norm.cdf(x_cdf)
    
    ax2.plot(x_cdf, y_cdf, 'g-', linewidth=2, label='CDF')
    ax2.axhline(0.5, color='gray', linestyle=':', alpha=0.7, label='50th percentile')
    ax2.axvline(0, color='gray', linestyle=':', alpha=0.7)
    
    # Mark some key points
    key_points = [-2, -1, 0, 1, 2]
    for point in key_points:
        cdf_val = norm.cdf(point)
        ax2.plot(point, cdf_val, 'ro', markersize=6)
        ax2.annotate(f'({point}, {cdf_val:.3f})', 
                    (point, cdf_val), 
                    xytext=(5, 5), textcoords='offset points', fontsize=8)
    
    ax2.set_xlabel('Z-Score')
    ax2.set_ylabel('Cumulative Probability')
    ax2.set_title('Cumulative Distribution Function (CDF)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def step_by_step_example():
    """Show step-by-step calculation for a specific z-score"""
    z = -1.0
    
    print(f"\n=== Step-by-Step Example: Z = {z} ===")
    print(f"Question: What percentile does z = {z} represent?")
    print()
    
    print("Step 1: Understand what we're looking for")
    print(f"   We want P(Z ≤ {z}) where Z ~ N(0,1)")
    print()
    
    print("Step 2: This equals the integral")
    print(f"   ∫_{-8}^{z} (1/√(2π)) * e^(-x²/2) dx")
    print()
    
    print("Step 3: Use norm.cdf() to compute this")
    cdf_result = norm.cdf(z)
    percentile = cdf_result * 100
    print(f"   norm.cdf({z}) = {cdf_result:.6f}")
    print()
    
    print("Step 4: Convert to percentile")
    print(f"   {cdf_result:.6f} × 100 = {percentile:.2f}%")
    print()
    
    print("Step 5: Interpretation")
    print(f"   {percentile:.2f}% of values in a standard normal distribution")
    print(f"   are less than or equal to {z}")
    print()
    
    # Verify with manual calculation
    manual_result = manual_cdf_approximation(z)
    print(f"Manual verification: {manual_result:.6f} (difference: {abs(cdf_result - manual_result):.2e})")

# Run all demonstrations
if __name__ == "__main__":
    demonstrate_cdf_calculation()
    compare_methods()
    step_by_step_example()
    
    print("\n" + "="*70)
    print("KEY TAKEAWAY:")
    print("norm.cdf(z) computes the area under the standard normal curve")
    print("from negative infinity up to z. This area represents the")
    print("proportion of values ≤ z, which when multiplied by 100")
    print("gives us the percentile.")
    print("="*70)
    
    # Uncomment the line below to see the visualization
    # visualize_cdf_concept()