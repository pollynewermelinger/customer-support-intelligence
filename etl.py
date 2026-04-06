import pandas as pd

def build_metrics(input_path='data/support_tickets.csv', output_path='data/metrics_summary.csv'):
    df = pd.read_csv(input_path, parse_dates=['created_at'])
    summary = pd.DataFrame({
        'metric': ['tickets', 'avg_first_response_time_min', 'avg_resolution_time_hours', 'avg_csat', 'sla_breach_rate'],
        'value': [len(df), round(df['first_response_time_min'].mean(), 2), round(df['resolution_time_hours'].mean(), 2), round(df['csat_score'].mean(), 2), round(df['sla_breached'].mean()*100, 2)]
    })
    summary.to_csv(output_path, index=False)
    print(f'Saved metrics to {output_path}')

if __name__ == '__main__':
    build_metrics()
