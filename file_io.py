def log_analyzing(input_file, output_file):
    total_lines = 0
    failure_count = 0
    warning_count = 0
    info_count = 0

    try:
        with open(input_file, 'r') as file:
            for line in file:
                total_lines += 1
                if 'failed' in line.lower():
                    failure_count += 1

                if 'warning' in line.lower():
                    warning_count += 1

                if 'info' in line.lower():
                    info_count += 1

    except FileNotFoundError:
        print(f'Error: {input_file} cannot be found!')
        return

    if failure_count > info_count and failure_count > warning_count:
        most_common = 'failed'

    elif warning_count > failure_count and warning_count > info_count:
        most_common = 'warning'

    else:
        most_common = 'info'

    with open(output_file, 'w') as report:
        report.write(f'There are a total of {total_lines} lines.\n')
        report.write(f'There are a total of {info_count} info lines.\n')
        report.write(f'There are a total of {warning_count} warnings!\n')
        report.write(f'There are a total of {failure_count} failures!!\n')
        report.write(f'The most common event type was: {most_common}')

    print('Log analysis complete !')
    print(f'This file analyzed {total_lines} lines in total.')
    print(f'This report has been saved to {output_file}')

log_analyzing('log.txt', 'report.txt')
