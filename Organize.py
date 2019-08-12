def log2json(log = str):

    log = log.split('\n')
    
    logFinal = {
        "installed": [],
        "upgraded": [],
        "removed": [],
        "full": []
    }
    
    for line in log:
        if '[ALPM] installed' in line:
            splitted = line.split()
            dictString = {
                'Date': splitted[0][1:] + ' ' + splitted[1][:-1],
                'Action': splitted[3],
                'Package': splitted[4],
                'Version': splitted[5][1:-1]
            }
            logFinal["installed"].append(dictString)
            logFinal["full"].append(dictString)

        elif '[ALPM] upgraded' in line:
            splitted = line.split()
            dictString = {
                'Date': splitted[0][1:] + ' ' + splitted[1][:-1],
                'Action': splitted[3],
                'Package': splitted[4],
                'Version': {
                    'older': splitted[5][1:],
                    'newer': splitted[7][:-1]
                }
            }
            logFinal["upgraded"].append(dictString)
            logFinal["full"].append(dictString)

        elif '[ALPM] removed' in line:
            splitted = line.split()
            dictString = {
                'Date': splitted[0][1:] + ' ' + splitted[1][:-1],
                'Action': splitted[3],
                'Package': splitted[4],
                'Version': splitted[5][1:-1]
            }
            logFinal["removed"].append(dictString)
            logFinal["full"].append(dictString)

    return dict(logFinal)
