import functions as fn

# "budget"
# "popularity"
# "release"
# "revenue"
# "runtime"
# "vote_average"
# "vote_count"

data = fn.get_data()

# fn.get_stats(data, ["budget", "vote_average", "vote_count", "revenue", "runtime", "popularity"])
fn.get_koefs(data.copy(), "vote_count", "revenue")
fn.get_koefs(data.copy(), "budget", "vote_count")
fn.get_koefs(data.copy(), "popularity", "revenue")
fn.get_koefs(data.copy(), "vote_average", "id")

fn.regression_analize(data.copy(), "popularity", "revenue")
fn.regression_analize(data.copy(), "vote_average", "id")
