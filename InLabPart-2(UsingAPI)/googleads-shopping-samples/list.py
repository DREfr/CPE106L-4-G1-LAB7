from google.ads.google_ads.client import GoogleAdsClient

def list_products(client, customer_id):
    # Google Ads Query Language (GAQL) query to retrieve product information
    query = """
        SELECT
            product.id,
            product.title,
            product.description
        FROM
            product
        LIMIT 10
    """

    # Get the Google Ads service client
    google_ads_service = client.get_service("GoogleAdsService")

    # Execute the query
    response = google_ads_service.search_stream(customer_id=customer_id, query=query)

    # Print the results
    for batch in response:
        for row in batch.results:
            print(f"Product ID: {row.product.id}, Title: {row.product.title}, Description: {row.product.description}")

def main():
    # Load Google Ads client from configuration (make sure to set up google-ads.yaml)
    client = GoogleAdsClient.load_from_storage()

    # Specify the customer ID (replace with your actual customer ID)
    customer_id = "INSERT_YOUR_CUSTOMER_ID_HERE"

    # List products
    list_products(client, customer_id)

if __name__ == "__main__":
    main()
