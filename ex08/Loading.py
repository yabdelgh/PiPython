def ft_tqdm(lst: range):
    goal = max(lst)
    for i in lst:
        progress = int(i / goal * 100)
        yield print(f"\r{progress}%|\033[41m{' ' * i}\033[0m\033[{goal}G| {i+1}/{goal+1}", end="")