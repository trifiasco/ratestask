query = '''
    SELECT p.code AS port FROM ports p JOIN (
        WITH RECURSIVE heirarchy(slug, parents) AS (
            SELECT r.slug, ARRAY[]::text[]
            FROM regions r WHERE parent_slug IS NULL

            UNION ALL

            SELECT regions.slug, (heirarchy.parents || regions.parent_slug)
            FROM regions, heirarchy
            WHERE regions.parent_slug = heirarchy.slug
        ) SELECT slug, parents 
          FROM heirarchy
          WHERE heirarchy.slug = %(slug)s or %(slug)s = ANY(heirarchy.parents)
    ) tree ON tree.slug = p.parent_slug
'''
