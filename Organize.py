def log2json(log = str):

    log = log.split('\n')

    def organize(line):
        output = []
        if '[ALPM] installed' in line:
            splitted = line.split()
            output = list([{
                'Date': splitted[0][1:] + ' ' + splitted[1][:-1],
                'Action': splitted[3],
                'Package': splitted[4],
                'Version': splitted[5][1:-1]
            }])

        elif '[ALPM] upgraded' in line:
            splitted = line.split()
            output = list([{
                'Date': splitted[0][1:] + ' ' + splitted[1][:-1],
                'Action': splitted[3],
                'Package': splitted[4],
                'Version': {
                    'older': splitted[5][1:],
                    'newer': splitted[7][:-1]
                }
            }])

        elif '[ALPM] removed' in line:
            splitted = line.split()
            output = list([{
                'Date': splitted[0][1:] + ' ' + splitted[1][:-1],
                'Action': splitted[3],
                'Package': splitted[4],
                'Version': splitted[5][1:-1]
            }])

        return output

    final = filter(organize, log)
    final = list(map(organize, final))

    logFinal = list([{
        "installed": list(filter((lambda line: line[0]['Action'] == 'installed'), final)),
        "upgraded": list(filter((lambda line: line[0]['Action'] == 'upgraded'), final)),
        "removed": list(filter((lambda line: line[0]['Action'] == 'removed'), final)),
        "full": final
    }])

    return list(logFinal)
