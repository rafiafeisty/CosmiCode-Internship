import pandas as pd
import threading
import logging
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from time import time
from typing import Optional, List, Tuple

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DataCleaner:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df: Optional[pd.DataFrame] = None
        self.cleaning_time: float = 0

    def load_data(self) -> None:
        try:
            start = time()
            self.df = pd.read_csv(self.file_path)
            logging.info(f"Data loaded successfully from {self.file_path}")
        except FileNotFoundError:
            logging.error("File not found! Please check the path.")
            raise
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            raise

    def clean_data(self) -> None:
        if self.df is None:
            raise ValueError("No data to clean. Load data first.")

        try:
            start = time()
            
            self.df.columns = self.df.columns.str.strip()
            
            if 'Sale_Date' in self.df.columns:
                self.df['Sale_Date'] = pd.to_datetime(self.df['Sale_Date'])
            
            numeric_cols = self.df.select_dtypes(include='number').columns
            self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].mean())
            
            self.df.drop_duplicates(inplace=True)
            
            self.cleaning_time = time() - start
            logging.info(f"Data cleaned in {self.cleaning_time:.2f} seconds")
            
        except Exception as e:
            logging.error(f"Error during cleaning: {str(e)}")
            raise

class DataProcessor:
    def __init__(self, cleaner: DataCleaner):
        self.cleaner = cleaner
        self.df_encoded: Optional[pd.DataFrame] = None
        self.processing_time: float = 0
        self.recommendations: List[str] = []

    def encode_data(self) -> None:
        """Encode categorical data"""
        if self.cleaner.df is None:
            raise ValueError("No data to process. Clean data first.")

        try:
            start = time()
            self.df_encoded = pd.get_dummies(self.cleaner.df, drop_first=True)
            self.processing_time = time() - start
            logging.info(f"Data encoded in {self.processing_time:.2f} seconds")
        except Exception as e:
            logging.error(f"Error during encoding: {str(e)}")
            raise

    def analyze_sales(self) -> List[str]:
        if self.cleaner.df is None:
            raise ValueError("No data to analyze. Clean data first.")

        try:
            self.recommendations = []
            
            if 'Sales_Amount' in self.cleaner.df.columns:
                if 'Product_Category' in self.cleaner.df.columns:
                    category_sales = self.cleaner.df.groupby('Product_Category')['Sales_Amount'].sum().sort_values()
                    low_performers = category_sales.head(2)
                    if not low_performers.empty:
                        self.recommendations.append(
                            f"Low-performing products: {', '.join(low_performers.index)}. "
                            "Consider promotions or discontinuing these categories."
                        )
                
                if 'Region' in self.cleaner.df.columns:
                    region_sales = self.cleaner.df.groupby('Region')['Sales_Amount'].sum().sort_values(ascending=False)
                    top_region = region_sales.head(1)
                    if not top_region.empty:
                        self.recommendations.append(
                            f"Top-performing region: {top_region.index[0]} with ${top_region.iloc[0]:.2f} in sales. "
                            "Allocate more resources here."
                        )
                
                if 'Sale_Date' in self.cleaner.df.columns:
                    self.cleaner.df['Month'] = self.cleaner.df['Sale_Date'].dt.month
                    monthly_sales = self.cleaner.df.groupby('Month')['Sales_Amount'].sum()
                    peak_month = monthly_sales.idxmax()
                    self.recommendations.append(
                        f"Peak sales in month {peak_month}. Plan major campaigns around this period."
                    )
            
            if not self.recommendations:
                self.recommendations.append("No specific recommendations due to limited data.")
            
            logging.info("Sales analysis completed")
            return self.recommendations
            
        except Exception as e:
            logging.error(f"Error during sales analysis: {str(e)}")
            raise

    def generate_plots(self) -> List[Tuple[str, str]]:
        if self.cleaner.df is None:
            raise ValueError("No data to plot. Clean data first.")

        plots = []
        try:
            if 'Sale_Date' in self.cleaner.df.columns and 'Sales_Amount' in self.cleaner.df.columns:
                plt.figure(figsize=(10, 6))
                self.cleaner.df.groupby('Sale_Date')['Sales_Amount'].sum().plot(kind='line', marker='o')
                plt.title('Sales Over Time', fontsize=14)
                plt.xlabel('Date', fontsize=12)
                plt.ylabel('Sales Amount ($)', fontsize=12)
                plt.grid(True)
                plt.xticks(rotation=45)
                plt.tight_layout()
                
                # Save plot to base64
                buffer = BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                plots.append(('Sales Over Time', f'data:image/png;base64,{image_base64}'))
                plt.close()

            # Plot 2: Sales by Product Category
            if 'Product_Category' in self.cleaner.df.columns and 'Sales_Amount' in self.cleaner.df.columns:
                plt.figure(figsize=(10, 6))
                self.cleaner.df.groupby('Product_Category')['Sales_Amount'].sum().plot(kind='bar')
                plt.title('Sales by Product Category', fontsize=14)
                plt.xlabel('Product Category', fontsize=12)
                plt.ylabel('Sales Amount ($)', fontsize=12)
                plt.grid(True)
                plt.xticks(rotation=45)
                plt.tight_layout()
                
                # Save plot to base64
                buffer = BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                plots.append(('Sales by Product Category', f'data:image/png;base64,{image_base64}'))
                plt.close()

            logging.info("Performance plots generated")
            return plots
            
        except Exception as e:
            logging.error(f"Error generating plots: {str(e)}")
            raise

class HTMLGenerator:
    def __init__(self, processor: DataProcessor):
        self.processor = processor
        self.generation_time: float = 0

    def generate_html(self, rows: int = 10) -> str:
        if self.processor.df_encoded is None:
            raise ValueError("No encoded data available.")

        try:
            start = time()
            table_data = self.processor.df_encoded.head(rows)
            html_table = table_data.to_html(classes='data-table', index=False)
            recommendations = self.processor.analyze_sales()
            plots = self.processor.generate_plots()
            recommendations_html = "<h2>Sales Improvement Recommendations</h2><ul>"
            for rec in recommendations:
                recommendations_html += f"<li>{rec}</li>"
            recommendations_html += "</ul>"

            plots_html = "<h2>Performance Visualizations</h2>"
            for title, img_data in plots:
                plots_html += f"""
                <h3>{title}</h3>
                <img src="{img_data}" alt="{title}" style="max-width: 100%; height: auto;">
                """

                html_content = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Cleaned Sales Data</title>
                    <style>
                        body {{
                            background-color: rgb(5, 69, 125);
                            color: white;
                            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                            margin: 0;
                            padding: 20px;
                        }}

                        .container {{
                            max-width: 1200px;
                            margin: auto;
                            background: rgba(255, 255, 255, 0.1);
                            padding: 30px;
                            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
                            border-radius: 12px;
                            backdrop-filter: blur(5px);
                        }}

                        h1, h2, h3 {{
                            color: white;
                        }}

                        /* Scrollable table container */
                        .table-container {{
                            width: 100%;
                            overflow-x: auto;
                            margin: 20px 0;
                            border: 1px solid rgba(255, 255, 255, 0.2);
                            border-radius: 8px;
                            background: rgba(255, 255, 255, 0.05);
                        }}

                        .data-table {{
                            width: 100%;
                            border-collapse: collapse;
                            min-width: 600px; /* Ensures table doesn't shrink too much */
                        }}

                        .data-table th,
                        .data-table td {{
                            border: 1px solid rgba(255, 255, 255, 0.2);
                            padding: 10px 12px;
                            text-align: center;
                        }}

                        .data-table th {{
                            background-color: rgba(52, 152, 219, 0.7);
                            color: white;
                            position: sticky;
                            top: 0;
                        }}

                        .data-table tr:nth-child(even) {{
                            background-color: rgba(255, 255, 255, 0.05);
                        }}

                        .data-table tr:hover {{
                            background-color: rgba(52, 152, 219, 0.2);
                        }}

                        .img-container {{
                            margin: auto;
                            margin-top: 20px;
                            border-radius: 10px;
                            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5);
                            max-width: 100%;
                        }}

                        .recommendation {{
                            margin-top: 20px;
                            padding: 15px;
                            background: rgba(255, 255, 255, 0.1);
                            border-radius: 8px;
                        }}

                        .section {{
                            margin-top: 40px;
                        }}

                        .section h2 {{
                            border-left: 5px solid #2980b9;
                            padding-left: 10px;
                            margin-bottom: 20px;
                        }}

                        /* Custom scrollbar */
                        ::-webkit-scrollbar {{
                            height: 8px;
                            width: 8px;
                        }}

                        ::-webkit-scrollbar-track {{
                            background: rgba(255, 255, 255, 0.1);
                            border-radius: 4px;
                        }}

                        ::-webkit-scrollbar-thumb {{
                            background: rgba(52, 152, 219, 0.5);
                            border-radius: 4px;
                        }}

                        ::-webkit-scrollbar-thumb:hover {{
                            background: rgba(52, 152, 219, 0.7);
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Cleaned Sales Data (First {rows} Rows)</h1>
                        
                        <div class="table-container">
                            {html_table}
                        </div>

                        <div class="section">
                            <h2>Recommendations</h2>
                            <div class="recommendation">
                                {recommendations_html}
                            </div>
                        </div>

                        <div class="section">
                            <h2>Visualizations</h2>
                            <div class="img-container">
                                {plots_html}
                            </div>
                        </div>
                    </div>
                </body>
                </html>
            """
            
            self.generation_time = time() - start
            logging.info(f"HTML generated in {self.generation_time:.2f} seconds")
            return html_content
            
        except Exception as e:
            logging.error(f"Error generating HTML: {str(e)}")
            raise

    def save_to_file(self, content: str, filename: str = "index.html") -> None:
        try:
            with open(filename, "w") as f:
                f.write(content)
            logging.info(f"File saved successfully as {filename}")
        except IOError as e:
            logging.error(f"Error saving file: {str(e)}")
            raise

def main():
    try:
        cleaner = DataCleaner("sales_data.csv")
        processor = DataProcessor(cleaner)
        html_gen = HTMLGenerator(processor)

        load_thread = threading.Thread(target=cleaner.load_data)
        clean_thread = threading.Thread(target=cleaner.clean_data)
        
        load_thread.start()
        load_thread.join()
        
        clean_thread.start()
        clean_thread.join() 

        processor.encode_data()
        html_content = html_gen.generate_html()
        html_gen.save_to_file(html_content)

        total_time = cleaner.cleaning_time + processor.processing_time + html_gen.generation_time
        logging.info(f"Total execution time: {total_time:.2f} seconds")

    except Exception as e:
        logging.error(f"Application error: {str(e)}")
        raise

if __name__ == "__main__":
    main()