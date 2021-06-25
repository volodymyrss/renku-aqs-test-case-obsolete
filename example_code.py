import click

@click.command()
@click.option("-r", "--ra", type=float, default=0)
@click.option("-a", "--autolog", is_flag=True)
def cli(ra, autolog):
    if autolog:
        import aqsconverters.aq 
        aqsconverters.aq.autolog()

    import astroquery.sdss

    print(astroquery.sdss.SDSS.query_region)

    r = astroquery.sdss.SDSS.query_region(f"{ra} 0", radius="0.001 deg")

    print("astroquery returns:", r)

    open("test-output.txt", "w").write("test!" + str(getattr(astroquery, 'hooked')))


cli()