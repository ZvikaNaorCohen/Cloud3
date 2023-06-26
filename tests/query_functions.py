import connectionController

def main():
    with open('query.txt', 'r') as query_file:
        counter = 0
        with open('response.txt', 'w') as response_file:
            for line in query_file:
                # Remove any leading/trailing whitespace
                counter = counter+1
                dish_name = line.strip()
                post_response = connectionController.http_post("dishes", data={'name': dish_name})
                get_response = connectionController.http_get(f"/dishes/{dish_name}")

                if(post_response.json() == -3 or post_response.json() == -4):
                    response_file.write(f'Food at line {counter} does not exist in Ninjas API, or Ninjas API is unreachable. Returned code -3 or -4.\n')
                    print(f'Food at line {counter} does not exist in Ninjas API. Returned code -3.')
                    continue

                sugar = get_response.json()['sugar']
                sodium = get_response.json()['sodium']
                calories = get_response.json()['cal']
                # Write to response.txt
                response_file.write(f'{dish_name} contains {calories} calories, {sodium} mgs of sodium, and {sugar} grams of sugar\n')
                print(f'{dish_name} contains {calories} calories, {sodium} mgs of sodium, and {sugar} grams of sugar')

if __name__ == "__main__":
    main()